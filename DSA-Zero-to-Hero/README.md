# DSA: Zero to Hero

**Read it online: <https://self-prep-seven.vercel.app/DSA-Zero-to-Hero/>**

Data structures and algorithms, one topic per notebook, each taken from "I have never
implemented this" to "I can build it from scratch, prove it correct, prove its cost, say what it
is bad at, and defend all of that in an interview".

The companion to [`../ML-Zero-to-Hero/`](../ML-Zero-to-Hero/), with a stricter quality bar —
because in this domain correctness and cost are *decidable*, so they get tested rather than
asserted.

**Progress: 4 of 23 complete.**

***

## Start here

| # | Notebook | What you get | Status |
|---|---|---|---|
| **00** | [`complexity_zero_to_hero.ipynb`](complexity_zero_to_hero.ipynb) | Big-O/Ω/Θ and what each is *for*, the cost model and **where it lies**, the doubling experiment, **amortised analysis three ways**, recurrences and the Master theorem **verified by counting**, and the stack depth you forgot to budget for | ✅ |
| **01** | [`arrays_zero_to_hero.ipynb`](arrays_zero_to_hero.ipynb) | Contiguity and the address formula, **the dynamic array from scratch in both languages**, the growth factor priced as a trade, the boxing tax, prefix sums and difference arrays derived rather than memorised — and **cache locality measured at 8x** | ✅ |
| **02** | [`strings_zero_to_hero.ipynb`](strings_zero_to_hero.ipynb) | Immutability and what it costs, **the concatenation trap measured on two axes** — CPython's `+=` is exactly O(n) under a megabyte and exactly O(n²) above it — KMP, the Z-algorithm and Rabin-Karp with the verification step people forget, and **why `len()` cannot tell you how many characters there are** | ✅ |
| **03** | [`hashing_zero_to_hero.ipynb`](hashing_zero_to_hero.ipynb) | What a hash function must guarantee (uniformity measured with a χ² test), **chaining and open addressing both built from scratch**, load factor measured against Knuth's formulas, the four core map patterns — and **the adversarial input that turns a `dict` quadratic**, with each of Python and Java defending the axis the other leaves open | ✅ |

**Read 00 first, whatever you are after.** It builds
[`dsa_toolkit.py`](dsa_toolkit.py) — the harness every other notebook imports — and it
establishes the habit the whole series runs on: *a complexity is something you measure, not
something you assert.*

## Still to come

**Linear structures** — 04 Linked Lists ·
05 Stacks, Queues & Deques

**Trees** — 06 Trees & Traversals · 07 Binary Search Trees · 08 Balanced Trees & B-Trees ·
09 Heaps & Priority Queues

**Specialised structures** — 10 Tries · 11 Disjoint Set Union · 12 Fenwick & Segment Trees

**Sorting and searching** — 13 Comparison Sorts & the Lower Bound · 14 Linear-Time Sorts &
Selection · 15 Binary Search & the Invariant Discipline

**Paradigms** — 16 Recursion & Divide and Conquer · 17 Backtracking · 18 Greedy Algorithms &
Exchange Arguments · 19 Dynamic Programming

**Graphs and bits** — 20 Graphs I: Representation & Traversal · 21 Graphs II: Shortest Paths,
MST & Flow · 22 Bit Manipulation

See [`DSA_ZERO_TO_HERO_PLAN.md`](DSA_ZERO_TO_HERO_PLAN.md) for the brief on each, the build
order, and the status log.

***

## What makes this series different

**Every implementation is written twice — Python and Java — and the two are checked against each
other on identical inputs.** That is not decoration. It catches a whole class of bug that neither
implementation reveals alone: integer overflow, division and modulo on negatives, sort stability,
iteration order. NB-00 §2.3 demonstrates it on a one-word change, `long` to `int`, where Python
reports 4,000,000,000 and Java reports −294,967,296.

**Every complexity claim is measured.** Timed at doubling sizes with the ratios printed, and the
fit reported alongside the runner-up. Where the measurement disagrees with the textbook bound,
the notebook investigates and explains the gap rather than dropping it — NB-00 §3.2 is exactly
that case, and it concludes that the experiment was too small rather than that the theory was
wrong.

**Every invariant is asserted in code**, after every operation, in a randomised stress test. Not
described in prose and hoped for.

**Every implementation is differentially tested** against a brute-force reference over at least
1,000 randomised inputs plus a fixed adversarial set — empty, one element, all-equal, sorted,
reverse sorted, many duplicates, and the 32-bit extremes. When a test fails, the harness
**minimises the input** before reporting it.

## How each notebook is laid out

| Part | Contents |
|---|---|
| **0** | Setup — imports and a JDK check |
| **1** | **Theory from zero** — the invariant, then the implementation from scratch in Python, then in Java, cross-checked; the cost, measured; the failure modes |
| **2** | **Worked problems** — solved in full, with the pattern named |
| **3** | The topic's signature difficulty, in depth |
| **4** | **Tough questions** — ~12 with hidden answers, plus 3 coding challenges |
| **5** | **Practice** — exercises ordered by difficulty, each with the trap it sets |
| **6** | **Reading** — the chapters and papers behind each section |
| — | Appendix — a symptom/cause/fix table and a checklist |

***

## Running them

```bash
pip install --upgrade pip        # nothing else: no third-party dependencies at all
```

A notebook about arrays should not need numpy in order to talk about arrays, so the series uses
only the Python standard library.

**For the Java half you need a JDK.** Part 0 of every notebook checks for one and tells you what
to do if it is missing:

```bash
winget install --id EclipseAdoptium.Temurin.21.JDK -e   # Windows
brew install --cask temurin                             # macOS
sudo apt install default-jdk                            # Debian/Ubuntu
```

Verified against **JDK 21.0.12 (Temurin)** and **Python 3.14**. Without a JDK the Python content
still runs; the Java cells print a skip notice instead.

Open a notebook in Jupyter or VS Code from *inside this folder* and run it top to bottom —
`dsa_toolkit.py` is imported as a sibling module, so the working directory matters.

## `dsa_toolkit.py`

The shared harness, built and explained in NB-00 Part 2.

| Function | What it does |
|---|---|
| `run_java(source, stdin=...)` | Compiles with `-Xlint:all -Werror` and runs; caches by source hash |
| `stress(impl, reference, gen)` | Differential testing, with the failing input minimised |
| `cross_check(py_fn, java_src, gen, to_stdin)` | The same, across the two languages |
| `measure_growth(fn, sizes)` | The doubling experiment |
| `fit_complexity(sizes, times)` | Which class the timings actually support, ranked |
| `growth_table(rows, claim=...)` | Prints the table and says whether it matches the claim |
| `check_invariant(structure, predicate)` | Asserts the property that defines a structure |
| `edge_cases(kind)` | The adversarial inputs random generation never produces |

***

## Also in this folder

`trackers/` holds the two DSA study-tracker notebooks this series is being built from — topic
checklists over the same ground, with no implementations, no measured complexity, no Java and no
proofs. `trackers/archive/` keeps the original combined tracker they were split from.

***

The repository root, [`../README.md`](../README.md), lists this series alongside the other
notebook collections here.
