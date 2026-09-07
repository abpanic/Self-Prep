#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Verify a zero-to-hero notebook: structure, then a full top-to-bottom execution.

The quality gate for both zero-to-hero series (see each series folder's README,
and DSA-Zero-to-Hero/DSA_ZERO_TO_HERO_PLAN.md for the DSA quality bar).
It exists in the repo (rather than a scratch directory) so it survives a context
reset and can be re-run by any future session.

Usage
-----
    python tools/verify_notebook.py <notebook.ipynb>            # structure only
    python tools/verify_notebook.py <notebook.ipynb> --run      # + execute all code
    python tools/verify_notebook.py <notebook.ipynb> --run --python <interpreter>

--run extracts every code cell in order into one script and executes it with
`warnings.simplefilter("error")`, so a warning fails the build exactly like an
exception. matplotlib is forced to the Agg backend and plt.show() is stubbed out.

Exit code 0 = clean, 1 = problems found.
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
import tempfile

NL = "\n"


def load(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def check_structure(nb):
    """Static checks. Returns a list of problem strings."""
    problems = []
    cells = nb["cells"]
    code = [c for c in cells if c["cell_type"] == "code"]

    ids = [c.get("id") for c in cells]
    if None in ids:
        problems.append("%d cell(s) missing an 'id'" % ids.count(None))
    dupes = {i for i in ids if i is not None and ids.count(i) > 1}
    if dupes:
        problems.append("duplicate cell ids: %s" % sorted(dupes)[:5])

    for i, c in enumerate(cells):
        if c["cell_type"] != "code":
            continue
        try:
            compile("".join(c["source"]), "cell-%d" % i, "exec")
        except SyntaxError as exc:
            problems.append("cell %d syntax error: %s" % (i, exc))

    # Machine-specific junk that must never be committed inside outputs.
    leaks = ("micromamba", "site-packages", "AppData", "Users" + os.sep)
    for i, c in enumerate(cells):
        for o in c.get("outputs") or []:
            text = "".join(o.get("text") or [])
            if o.get("name") == "stderr" and text.strip():
                problems.append("cell %d has stderr baked into its saved output" % i)
            for needle in leaks:
                if needle in text:
                    problems.append("cell %d output leaks a local path (%r)" % (i, needle))
                    break

    # Run-state consistency. The real invariant is one-directional: a cell that has
    # OUTPUTS must have been executed, so it must carry an execution_count. The reverse
    # is not true - a cell can run and print nothing, which is perfectly normal.
    orphan_outputs = [i for i, c in enumerate(cells)
                      if c["cell_type"] == "code" and c.get("outputs")
                      and c.get("execution_count") is None]
    if orphan_outputs:
        problems.append(
            "%d cell(s) have saved outputs but no execution_count (a tool stripped the "
            "counts and kept the outputs): cells %s"
            % (len(orphan_outputs), orphan_outputs[:8]))

    # Edit-history archaeology: references to versions of the file itself.
    for i, c in enumerate(cells):
        for line in "".join(c["source"]).split(NL):
            if re.search(r"\bv[1-9]\b (?:bug|fix|note|addition)|in v[1-9] we", line, re.I):
                problems.append("cell %d references its own edit history: %s"
                                % (i, line.strip()[:70]))
    return problems


def build_runner(nb, path):
    """Write every code cell, in order, into one executable script."""
    lines = [
        "import matplotlib",
        "matplotlib.use('Agg')",
        "import matplotlib.pyplot as _plt",
        "_plt.show = lambda *a, **k: None",
        "import warnings",
        "warnings.simplefilter('error')",
    ]
    n = 0
    for c in nb["cells"]:
        if c["cell_type"] != "code":
            continue
        n += 1
        lines.append("print('--- cell %d (%s) ---')" % (n, c.get("id")))
        lines.append("".join(c["source"]))
    lines.append("print()")
    lines.append("print('ALL %d CODE CELLS RAN CLEAN')" % n)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(NL.join(lines))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("notebook")
    ap.add_argument("--run", action="store_true", help="execute every code cell in order")
    ap.add_argument("--python", default=sys.executable,
                    help="interpreter to execute with (needs numpy/pandas/sklearn/matplotlib)")
    args = ap.parse_args()

    nb = load(args.notebook)
    cells = nb["cells"]
    n_code = sum(1 for c in cells if c["cell_type"] == "code")
    print("%s" % args.notebook)
    print("  nbformat %d.%d | %d cells (%d code, %d markdown)"
          % (nb["nbformat"], nb["nbformat_minor"], len(cells), n_code, len(cells) - n_code))

    problems = check_structure(nb)
    if problems:
        print("  STRUCTURE: %d problem(s)" % len(problems))
        for p in problems:
            print("    - %s" % p)
    else:
        print("  STRUCTURE: clean")

    if args.run:
        tmp = os.path.join(tempfile.gettempdir(), "_verify_run.py")
        total = build_runner(nb, tmp)
        print("  EXECUTING %d code cells with warnings-as-errors ..." % total)
        # Run from the notebook's own directory, which is what Jupyter does. Without
        # this a notebook that imports a module sitting beside it (e.g. DSA-Zero-to-
        # Hero/dsa_toolkit.py) passes in Jupyter and fails here, for no real reason.
        workdir = os.path.dirname(os.path.abspath(args.notebook)) or None
        proc = subprocess.run([args.python, tmp], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", cwd=workdir)
        out = (proc.stdout or "") + (proc.stderr or "")
        if proc.returncode == 0 and "ALL %d CODE CELLS RAN CLEAN" % total in out:
            print("  EXECUTION: clean")
        else:
            print("  EXECUTION: FAILED")
            problems.append("execution failed")
            print(NL.join(out.strip().split(NL)[-25:]))

    print("  RESULT: %s" % ("PASS" if not problems else "FAIL"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
