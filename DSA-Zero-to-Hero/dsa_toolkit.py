# -*- coding: utf-8 -*-
"""The shared harness for the DSA: Zero to Hero series.

Every notebook in the series imports from here. It exists so that the quality bar
in DSA_ZERO_TO_HERO_PLAN.md section 6 is cheap enough to actually hold to:

    1. every implementation differentially tested against a reference
    2. Python and Java tested against each other on identical inputs
    3. every complexity measured, not asserted
    4. every invariant asserted in code

NB-00 builds this module up from nothing and explains each part. It is written out
here so the other 22 notebooks can just import it.

No third-party dependencies, by design: a notebook about arrays should not need
numpy to talk about arrays.
"""
from __future__ import annotations

import hashlib
import math
import os
import random
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import time

__all__ = [
    "java_available", "run_java", "JavaError",
    "stress", "cross_check", "StressFailure",
    "measure_growth", "fit_complexity", "growth_table",
    "check_invariant", "InvariantError",
    "edge_cases",
]


# ===========================================================================
# Java
# ===========================================================================

class JavaError(RuntimeError):
    """javac or java failed. The message carries the compiler/runtime output."""


_JAVA_CACHE_DIR = os.path.join(tempfile.gettempdir(), "dsa_toolkit_java")
_CLASS_RE = re.compile(r"(?:^|\s)(?:public\s+)?(?:final\s+)?class\s+(\w+)", re.M)


def _find_tool(name):
    """Locate javac/java: PATH, then JAVA_HOME, then the usual Windows install dirs."""
    found = shutil.which(name)
    if found:
        return found
    home = os.environ.get("JAVA_HOME")
    if home:
        cand = os.path.join(home, "bin", name + (".exe" if os.name == "nt" else ""))
        if os.path.exists(cand):
            return cand
    if os.name == "nt":
        roots = [r"C:\Program Files\Eclipse Adoptium", r"C:\Program Files\Java",
                 r"C:\Program Files\Microsoft"]
        for root in roots:
            if not os.path.isdir(root):
                continue
            for entry in sorted(os.listdir(root), reverse=True):   # newest-looking first
                cand = os.path.join(root, entry, "bin", name + ".exe")
                if os.path.exists(cand):
                    return cand
    return None


def java_available():
    """(ok, message). Call this in Part 0 so a missing JDK fails loudly and early."""
    javac, java = _find_tool("javac"), _find_tool("java")
    if not javac or not java:
        return False, ("No JDK found. Install one, then restart the kernel:\n"
                       "    winget install --id EclipseAdoptium.Temurin.21.JDK -e")
    try:
        out = subprocess.run([javac, "--version"], capture_output=True, text=True,
                             timeout=60)
        return True, (out.stdout or out.stderr).strip()
    except Exception as exc:                                    # pragma: no cover
        return False, "javac found at %s but would not run: %s" % (javac, exc)


def _class_name(source):
    m = _CLASS_RE.search(source)
    if not m:
        raise JavaError("could not find a class declaration in the Java source")
    return m.group(1)


def run_java(source, stdin="", timeout=120, args=()):
    """Compile and run a self-contained Java program; return its stdout.

    Compiles with -Xlint:all -Werror, so a Java warning fails the build exactly as
    a Python warning does under warnings.simplefilter("error").

    The compiled class is cached under the system temp directory, keyed by a hash of
    the source, so re-running a notebook does not recompile anything.
    """
    javac, java = _find_tool("javac"), _find_tool("java")
    if not javac or not java:
        ok, msg = java_available()
        raise JavaError(msg)

    cls = _class_name(source)
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]
    outdir = os.path.join(_JAVA_CACHE_DIR, digest)
    marker = os.path.join(outdir, cls + ".class")

    if not os.path.exists(marker):
        os.makedirs(outdir, exist_ok=True)
        src_path = os.path.join(outdir, cls + ".java")
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(source)
        proc = subprocess.run([javac, "-Xlint:all", "-Werror", "-d", outdir, src_path],
                              capture_output=True, text=True, timeout=timeout)
        if proc.returncode != 0:
            shutil.rmtree(outdir, ignore_errors=True)   # never cache a failed build
            raise JavaError("javac failed:\n" + (proc.stderr or proc.stdout))

    proc = subprocess.run([java, "-cp", outdir, cls, *map(str, args)],
                          input=stdin, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise JavaError("java exited %d:\n%s" % (proc.returncode,
                                                 proc.stderr or proc.stdout))
    return proc.stdout


# ===========================================================================
# Differential testing
# ===========================================================================

class StressFailure(AssertionError):
    """An implementation disagreed with its reference. Carries the minimised input."""


def _shrink(case, still_fails):
    """Crudely minimise a failing input: drop elements while it keeps failing.

    Not a general shrinker — it handles lists and strings, which is what these
    notebooks generate. A smaller counterexample is worth a lot when debugging.
    """
    if not isinstance(case, (list, str)):
        return case
    changed = True
    while changed and len(case) > 1:
        changed = False
        for i in range(len(case)):
            smaller = case[:i] + case[i + 1:]
            if len(smaller) and still_fails(smaller):
                case, changed = smaller, True
                break
    return case


def stress(impl, reference, gen, n=1000, seed=0, extra=(), label=""):
    """Run `impl` and `reference` on n generated inputs; assert they always agree.

    gen(rng) -> one input. `impl` and `reference` each take that input and return a
    comparable result. Inputs in `extra` (e.g. from edge_cases()) are tested first,
    because the interesting failures are almost always there.

    Returns the number of cases checked. Raises StressFailure with a minimised
    counterexample on the first disagreement.
    """
    rng = random.Random(seed)

    def disagrees(case):
        try:
            a = impl(case)
        except Exception as exc:
            return ("impl raised %s: %s" % (type(exc).__name__, exc), None)
        b = reference(case)
        return None if a == b else (a, b)

    cases = list(extra) + [gen(rng) for _ in range(n)]
    for case in cases:
        bad = disagrees(case)
        if bad is not None:
            small = _shrink(case, lambda c: disagrees(c) is not None)
            raise StressFailure(
                "%s%s\n  failing input : %r\n  implementation: %r\n  reference     : %r"
                % (label + ": " if label else "", "implementation disagrees with reference",
                   small, bad[0], bad[1]))
    return len(cases)


def cross_check(py_fn, java_source, gen, to_stdin, n=200, seed=0, label=""):
    """Run a Python function and a Java program on identical inputs; assert agreement.

    to_stdin(case) -> the text handed to the Java program on stdin. The Java program
    prints its answer; it is compared against str(py_fn(case)).strip().

    This is the check that catches what neither language reveals alone: integer
    overflow, division and modulo semantics, sort stability, iteration order.
    """
    rng = random.Random(seed)
    for _ in range(n):
        case = gen(rng)
        want = str(py_fn(case)).strip()
        got = run_java(java_source, stdin=to_stdin(case)).strip()
        if want != got:
            raise StressFailure(
                "%sPython and Java disagree\n  input : %r\n  python: %s\n  java  : %s"
                % (label + ": " if label else "", case, want, got))
    return n


# ===========================================================================
# Measuring complexity
# ===========================================================================

def measure_growth(fn, sizes, setup=None, repeats=5):
    """Time fn at each size and report the ratio between consecutive sizes.

    fn(payload) is timed, where payload = setup(n) if setup is given else n. The
    setup cost is excluded. The MINIMUM of `repeats` runs is used, not the mean:
    timing noise is one-sided, so the minimum is the closest thing to the true cost.

    Returns a list of dicts: {n, seconds, ratio}. `ratio` is this size's time
    divided by the previous size's, which is the number that identifies the
    complexity class when the sizes double: ~1 is O(1), ~2 is O(n), slightly over 2
    is O(n log n), ~4 is O(n^2).
    """
    rows = []
    previous = None
    for n in sizes:
        best = math.inf
        for _ in range(repeats):
            payload = setup(n) if setup else n
            start = time.perf_counter()
            fn(payload)
            best = min(best, time.perf_counter() - start)
        rows.append({"n": n, "seconds": best,
                     "ratio": (best / previous) if previous else None})
        previous = best
    return rows


_MODELS = [
    ("O(1)", lambda n: 1.0),
    ("O(log n)", lambda n: math.log(max(n, 2), 2)),
    ("O(n)", lambda n: float(n)),
    ("O(n log n)", lambda n: n * math.log(max(n, 2), 2)),
    ("O(n^2)", lambda n: float(n) ** 2),
    ("O(n^3)", lambda n: float(n) ** 3),
    ("O(2^n)", lambda n: 2.0 ** min(n, 60)),
]


# Two candidate fits closer than this ratio in relative error are treated as
# indistinguishable by growth_table. 1.3 was chosen because O(n) and O(n log n)
# over an 8x range of sizes land around 1.0-1.2 apart on noisy timings, while a
# genuinely wrong candidate (O(n^2) against O(n log n), say) is off by 10x or more.
SEPARABLE_MARGIN = 1.3


def fit_complexity(sizes, times):
    """Which complexity class best explains these timings?

    For each candidate f, fit the single scale factor c that minimises the squared
    RELATIVE error of c*f(n) against the measurements — relative, because absolute
    error would let the largest size decide everything on its own.

    Returns a list of (name, relative_error) sorted best first. Use the top entry,
    but look at the second: when the two are close the measurement cannot tell them
    apart, and saying so is more honest than picking one.
    """
    sizes = [float(n) for n in sizes]
    times = [float(t) for t in times]
    out = []
    for name, f in _MODELS:
        fv = [f(n) for n in sizes]
        num = sum((t / v) for t, v in zip(times, fv) if v > 0)
        den = sum(1.0 for v in fv if v > 0)
        if den == 0:
            continue
        c = num / den                       # least squares in relative terms
        err = math.sqrt(statistics.fmean([((c * v - t) / t) ** 2
                                          for t, v in zip(times, fv) if t > 0]))
        out.append((name, err))
    return sorted(out, key=lambda p: p[1])


def growth_table(rows, claim=None, fit=True):
    """Print a measure_growth() result, and say whether it matches `claim`."""
    print("%10s %14s %10s" % ("n", "seconds", "ratio"))
    print("-" * 36)
    for r in rows:
        ratio = "%10.2f" % r["ratio"] if r["ratio"] else "%10s" % "-"
        print("%10s %14.6f %s" % ("{:,}".format(r["n"]), r["seconds"], ratio))
    if not fit:
        return None
    ranked = fit_complexity([r["n"] for r in rows], [r["seconds"] for r in rows])
    best, err = ranked[0]
    runner, err2 = ranked[1]
    print()
    print("best fit: %s (relative error %.3f); next: %s (%.3f)" % (best, err, runner, err2))

    # When the top two are within a whisker of each other the experiment simply
    # cannot separate them, and naming a winner would be false precision. This
    # happens constantly for O(n) vs O(n log n) over a narrow range of sizes --
    # see NB-00 section 3.2, which is about exactly this.
    separable = err2 > err * SEPARABLE_MARGIN
    if not separable:
        print("NOT SEPARABLE: %s and %s fit these timings about equally well."
              % (best, runner))
        print("  Read the ratio column instead, and widen the range of sizes or")
        print("  count operations rather than timing them (NB-00 1.7) if you need")
        print("  to settle it.")

    if claim:
        if best == claim:
            print("claimed %s -> measurement MATCHES the claim" % claim)
        elif not separable and runner == claim:
            print("claimed %s -> CONSISTENT with the measurement, which cannot"
                  % claim)
            print("  distinguish it from %s here." % best)
        else:
            print("claimed %s -> measurement does NOT match the claim" % claim)
            print("  Do not paper over this. Either the claim is wrong, the input never")
            print("  reaches the worst case, or constant factors dominate at these sizes.")
    return ranked


# ===========================================================================
# Invariants
# ===========================================================================

class InvariantError(AssertionError):
    """A structure violated the invariant that defines it."""


def check_invariant(structure, predicate, label="invariant", context=""):
    """Assert that `structure` satisfies `predicate`. Call it after EVERY operation.

    The difference between a prose claim and a verified one. `predicate` may return
    False, or a string explaining the violation.
    """
    result = predicate(structure)
    if result is not True:
        detail = result if isinstance(result, str) else "predicate returned %r" % (result,)
        raise InvariantError("%s violated%s: %s\n  state: %r"
                             % (label, (" after " + context) if context else "",
                                detail, structure))
    return True


# ===========================================================================
# Adversarial inputs
# ===========================================================================

def edge_cases(kind="ints", n=64, seed=0):
    """The standard inputs that break implementations, for a given input type.

    Every stress test in the series passes these through `extra=`. They are listed
    explicitly rather than generated at random because random inputs almost never
    produce them: an empty list, a single element, all-equal values, already sorted,
    reverse sorted, and the extremes of the integer range.
    """
    rng = random.Random(seed)
    if kind == "ints":
        big = 2 ** 31 - 1
        return [
            [], [0], [1], [-1],
            [0, 0], [1, 1, 1, 1],
            list(range(n)),                       # already sorted
            list(range(n, 0, -1)),                # reverse sorted
            [5] * n,                              # all equal
            [0, 1] * (n // 2),                    # many duplicates
            [big, -big - 1, 0],                   # 32-bit extremes: Java overflow bait
            [big, big],                           # sum overflows a Java int
            sorted(rng.randrange(-n, n) for _ in range(n)),
            [rng.randrange(-n, n) for _ in range(n)],
        ]
    if kind == "strings":
        return ["", "a", "aa", "ab", "aaaa", "abab", "a" * n,
                "".join(rng.choice("ab") for _ in range(n)),
                "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))]
    if kind == "sorted_ints":
        return [c for c in edge_cases("ints", n, seed) if c == sorted(c)]
    raise ValueError("unknown kind %r; expected 'ints', 'strings' or 'sorted_ints'" % kind)
