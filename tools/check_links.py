# -*- coding: utf-8 -*-
"""Check that every relative markdown link in the series resolves to a real file.

Covers the root and per-series READMEs, the DSA plan, and the markdown cells of
every notebook in both ML-Zero-to-Hero/ and DSA-Zero-to-Hero/. External links
(http/https/mailto) and bare anchors are skipped.

Run from the repo root after adding, renaming or moving a notebook:

    python tools/check_links.py

Exits non-zero if anything is broken, so it can gate a commit.
"""
import io
import json
import os
import re
import sys

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "#", "mailto:")

DOCS = [
    "README.md",
    "ML-Zero-to-Hero/README.md",
    "DSA-Zero-to-Hero/README.md",
    "DSA-Zero-to-Hero/DSA_ZERO_TO_HERO_PLAN.md",
]
NOTEBOOK_DIRS = ["ML-Zero-to-Hero", "DSA-Zero-to-Hero"]


def collect(root):
    """Yield (repo-relative path, markdown text) for everything worth checking."""
    for rel in DOCS:
        path = os.path.join(root, rel)
        if os.path.exists(path):
            yield rel, io.open(path, encoding="utf-8").read()

    for nbdir_rel in NOTEBOOK_DIRS:
        nbdir = os.path.join(root, nbdir_rel)
        if not os.path.isdir(nbdir):
            continue
        for name in sorted(os.listdir(nbdir)):
            if not name.endswith(".ipynb"):
                continue
            nb = json.load(io.open(os.path.join(nbdir, name), encoding="utf-8"))
            text = "\n".join("".join(c["source"]) for c in nb["cells"]
                             if c["cell_type"] == "markdown")
            yield nbdir_rel + "/" + name, text


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    total = 0
    broken = []

    for rel, text in collect(root):
        base = os.path.dirname(os.path.join(root, rel))
        bad = []
        for _, href in LINK.findall(text):
            href = href.split()[0].strip("<>")
            if href.startswith(SKIP_PREFIXES):
                continue
            total += 1
            # strip any #anchor before testing the path
            target = os.path.normpath(os.path.join(base, href.split("#")[0]))
            if not os.path.exists(target):
                bad.append(href)
        broken.extend((rel, h) for h in bad)
        print("%-58s %s" % (rel, "BROKEN %d" % len(bad) if bad else "ok"))
        for h in bad:
            print("      -> " + h)

    print()
    print("%d relative links checked, %d broken" % (total, len(broken)))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
