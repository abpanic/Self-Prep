# DSA: Zero to Hero — build plan, quality bar and status log

This file is for **whoever is building the series** (including a future session of mine that has
lost all context). It holds the roster, the quality bar, the build workflow, a brief for every
notebook, and an append-only status log.

A reader-facing `README.md` will live beside it once the first notebook lands. Keep the two
distinct: that one is for the student, this one is for the builder.

> **Precedent:** this series follows `ML-Zero-to-Hero/`, 16 notebooks and 952 cells, completed
> 2026-09-07. Its build plan was deleted once the series finished. What is reused here is the
> template, the quality bar and `tools/verify_notebook.py`. What is *new* is that every claim in
> DSA is a claim about **correctness and cost**, which can be tested far more sharply than an ML
> claim can — so the quality bar is stricter, not looser (§6).

***

## 1. The promise

Each notebook takes one data structure or algorithm from "I have never implemented this" to
"I can build it from scratch, prove it correct, prove its cost, say what it is bad at, and
defend all of that in an interview".

Three decisions set by the owner on 2026-09-07, all at the demanding end:

| Decision | Choice | What it costs |
|---|---|---|
| **Language** | **Python and Java side by side** | Every implementation written twice, and both verified. ~2x the code, ~1.4x the wall-clock. |
| **Granularity** | **Finer-grained, ~22 notebooks** | The natural split lands at **23** (§3). Big topics get room: sorting is two notebooks, graphs are two. |
| **Emphasis** | **Foundations first** | Amortised analysis, loop invariants, correctness arguments and measured complexity lead. Interview patterns follow from them rather than the other way round. |

**What "foundations first" means concretely**, since it is the choice that shapes every notebook:

- A structure is not introduced by its API. It is introduced by the **invariant** it maintains,
  and that invariant is then **asserted in code** after every operation in a randomised stress
  test — not merely described in prose.
- A complexity is never asserted. It is **measured** — timed at doubling input sizes, with the
  ratio printed — and where the measurement disagrees with the textbook bound, the notebook
  investigates and explains the gap instead of hiding it.
- A greedy algorithm comes with an **exchange argument**. A divide-and-conquer algorithm comes
  with its **recurrence** and the Master-theorem case it falls under. A DP comes with its
  **optimal-substructure statement** written out.
- Interview problems are Part 2 of each notebook, and they exist to exercise the foundation, not
  to be memorised.

***

## 2. Prerequisites and environment

### ⚠️ Blocker: there is no JDK on this machine

Checked 2026-09-07: `java`, `javac`, `jshell`, `mvn`, `gradle` are **all absent**, `JAVA_HOME` is
unset, and no JDK exists under `C:\Program Files\Java`, `Eclipse Adoptium`, `Microsoft\jdk*` or
`%LOCALAPPDATA%\Programs\Java`. `winget` **is** available.

**Nothing in the Java half of this series can be verified until a JDK is installed.** The build
must not start before this is resolved, because shipping unverified Java would violate quality-bar
rule 1 on the very first notebook.

```powershell
# Temurin 21 LTS is the safe default. Run this in a normal (non-elevated) PowerShell:
winget install --id EclipseAdoptium.Temurin.21.JDK -e
# then open a NEW shell and confirm:
javac --version    # expect: javac 21.x.x
java --version
```

Record the exact version in §10 when it is done. If the owner would rather not install a JDK, the
language decision in §1 has to be revisited — say so and stop, do not silently ship unrun Java.

### The rest of the environment

Inherited from the ML series and re-confirmed 2026-09-07:

- The notebook kernel is a conda env named **`base`** that is **not on PATH** from the shell.
- `python` on PATH is **3.14.7** with no third-party packages.
- So: create a throwaway venv per session to verify notebooks. It will not exist in a new session.

```bash
python -m venv <scratch>/venv
<scratch>/venv/Scripts/python.exe -m pip install -q numpy pandas matplotlib
```

DSA needs far fewer packages than ML did. `numpy`/`pandas` are for the benchmarking tables and
plots only — **no notebook may use them inside an implementation.** Every structure and algorithm
is written against the standard library alone, in both languages.

### Shell gotcha, inherited and still true

The Bash tool here mangles some heredocs — a heredoc body containing backslash escapes or certain
quoting can fail to parse, and the whole command then silently does nothing. Two rules that were
learned the hard way:

- Write non-trivial scripts with the `Write` tool, not with `cat > file <<'EOF'`.
- After any script writes a file, **re-read it** before trusting it.

### The VSCode hazard, inherited and still true

If a target `.ipynb` is open in VSCode, an editor save silently overwrites anything a script wrote
to disk. After writing a notebook, re-read it from disk to confirm the change survived, and tell
the owner to close the file first.

***

## 3. The roster

23 notebooks. Status legend: ⬜ not started · 🟡 in progress · ✅ complete and verified.

| # | Notebook | File | Status | Cells | Verified |
|---|---|---|---|---|---|
| 00 | **Complexity, Amortised Analysis & the Measurement Harness** | `complexity_zero_to_hero.ipynb` | ✅ | 54 (28 code) | ✅ struct + run |
| 01 | **Arrays & Dynamic Arrays** | `arrays_zero_to_hero.ipynb` | ✅ | 43 (21 code) | ✅ struct + run |
| 02 | **Strings & String Algorithms** | `strings_zero_to_hero.ipynb` | ✅ | 39 (18 code) | ✅ struct + run |
| 03 | **Hashing & Hash Tables** | `hashing_zero_to_hero.ipynb` | ✅ | 58 (23 code) | ✅ struct + run |
| 04 | **Linked Lists** | `linked_lists_zero_to_hero.ipynb` | ✅ | 56 (21 code) | ✅ struct + run |
| 05 | **Stacks, Queues & Deques** | `stacks_queues_zero_to_hero.ipynb` | ✅ | 50 (18 code) | ✅ struct + run |
| 06 | **Trees & Traversals** | `trees_zero_to_hero.ipynb` | ⬜ | — | — |
| 07 | **Binary Search Trees** | `bst_zero_to_hero.ipynb` | ⬜ | — | — |
| 08 | **Balanced Trees & B-Trees** | `balanced_trees_zero_to_hero.ipynb` | ⬜ | — | — |
| 09 | **Heaps & Priority Queues** | `heaps_zero_to_hero.ipynb` | ⬜ | — | — |
| 10 | **Tries** | `tries_zero_to_hero.ipynb` | ⬜ | — | — |
| 11 | **Disjoint Set Union** | `dsu_zero_to_hero.ipynb` | ⬜ | — | — |
| 12 | **Fenwick & Segment Trees** | `range_queries_zero_to_hero.ipynb` | ⬜ | — | — |
| 13 | **Sorting I: Comparison Sorts & the Lower Bound** | `sorting_comparison_zero_to_hero.ipynb` | ⬜ | — | — |
| 14 | **Sorting II: Linear-Time Sorts & Selection** | `sorting_linear_zero_to_hero.ipynb` | ⬜ | — | — |
| 15 | **Binary Search & the Invariant Discipline** | `binary_search_zero_to_hero.ipynb` | ⬜ | — | — |
| 16 | **Recursion & Divide and Conquer** | `recursion_zero_to_hero.ipynb` | ⬜ | — | — |
| 17 | **Backtracking** | `backtracking_zero_to_hero.ipynb` | ⬜ | — | — |
| 18 | **Greedy Algorithms & Exchange Arguments** | `greedy_zero_to_hero.ipynb` | ⬜ | — | — |
| 19 | **Dynamic Programming** | `dynamic_programming_zero_to_hero.ipynb` | ⬜ | — | — |
| 20 | **Graphs I: Representation & Traversal** | `graphs_traversal_zero_to_hero.ipynb` | ⬜ | — | — |
| 21 | **Graphs II: Shortest Paths, MST & Flow** | `graphs_paths_zero_to_hero.ipynb` | ⬜ | — | — |
| 22 | **Bit Manipulation** | `bit_manipulation_zero_to_hero.ipynb` | ⬜ | — | — |

**6 of 23 done.**

### Why 23 and not 22

The owner asked for ~22 and the natural split lands one over. The three places it would be
tempting to merge, and why each stays split:

- **Sorting I / II.** The Ω(n log n) comparison lower bound is a *proof*, and it is the whole
  reason linear-time sorts have to escape the comparison model. Merging buries the argument.
- **Graphs I / II.** Traversal is a structure topic; shortest paths and MST are an optimisation
  topic with their own proof obligations (Dijkstra's greedy-choice argument, the cut property).
- **BST / Balanced Trees.** A BST is defined by its invariant; a balanced tree is defined by a
  *second* invariant layered on top and the rotations that restore it. That layering is the lesson.

### Suggested build order

Not the reading order. Build in this order so that each notebook's tooling and cross-references
already exist when it is written:

1. **NB-00 first and alone.** It builds `dsa_toolkit.py` (§5), which every other notebook imports.
   Nothing else can be verified to the standard in §6 until it exists.
2. **NB-01 → 05** (linear structures) — they establish the amortised-analysis pattern.
3. **NB-13 → 16** (sorting, binary search, recursion) — they are the most self-contained, and
   NB-16's recurrence machinery is needed by the tree notebooks.
4. **NB-06 → 12** (trees and the specialised structures).
5. **NB-17 → 19** (backtracking, greedy, DP).
6. **NB-20 → 22** (graphs, bit manipulation).

***

## 4. Source material already in the repo

Two existing notebooks map the territory and should be mined, then superseded — the same
relationship the ML series had with `ml_study_tracker_*`. Leave them in place.

| File | Size | What to take from it |
|---|---|---|
| `trackers/core_swe_dsa_tracker_1_data_structures.ipynb` | 170 cells, 77 code | Topic checklists for arrays, hashing, stacks/queues, linked lists, trees, BSTs, heaps, graphs, advanced graphs, tree DP, tries, DSU. Its "common problems" lists are a good starting set for each Part 2. |
| `trackers/core_swe_dsa_tracker_2_algorithms.ipynb` | 181 cells, 82 code | Complexity, sorting, binary search, recursion, backtracking, sliding window, two pointers, greedy, DP, BFS/DFS, shortest paths, topological sort, bit manipulation. Ends with a Problem Log worth preserving as a pattern. |
| `../SWE_breadth_topics.ipynb` | — | Adjacent, not DSA. Out of scope; do not fold in. |

**What the trackers do not have, and this series must:** no from-scratch implementations held to
a correctness test, no measured complexity, no Java, no proofs, no "what this is bad at". They are
checklists. This series is the thing the checklists point at.

**Two patterns in the trackers worth keeping.** The per-topic *study checklist* maps well onto
this series' Part 4 questions, and the *Problem Log* at the end of tracker 2 is a good model for a
running record — consider a `PROBLEM_LOG.md` in this folder once a few notebooks exist.

***

## 5. Where the files live

```
Self-Prep/
├── README.md                       <- repo root; add a DSA section when NB-00 lands
├── ML-Zero-to-Hero/                <- the ML series, its trackers, practicals and data
├── DSA-Zero-to-Hero/
│   ├── DSA_ZERO_TO_HERO_PLAN.md    <- this file
│   ├── README.md                   <- reader-facing guide (create with NB-00)
│   ├── dsa_toolkit.py              <- the shared harness (built by NB-00)
│   ├── <topic>_zero_to_hero.ipynb  <- 23 notebooks
│   └── trackers/                    <- the study trackers this series supersedes
└── tools/
    ├── verify_notebook.py          <- the quality gate, reused unchanged
    └── check_links.py              <- relative-link checker, reused unchanged
```

### `dsa_toolkit.py` — the shared harness

NB-00 builds this from scratch, explains every part, and writes it to disk; every later notebook
does `from dsa_toolkit import ...`. It is the thing that makes the quality bar in §6 cheap enough
to actually hold to. Required contents:

| Function | What it does |
|---|---|
| `run_java(source, stdin="", classname=None)` | Writes a `.java` to a temp dir, compiles with `javac -Xlint:all -Werror`, runs it, returns stdout. Caches by source hash so re-running a notebook is fast. Raises with the compiler output on failure. |
| `stress(impl, reference, gen, n=1000, seed=0)` | Runs `impl` and `reference` on `n` randomly generated inputs and asserts identical output. Prints the **first failing input, minimised**, when they differ. |
| `cross_check(py_fn, java_source, gen, n=200)` | The same, across languages: feeds identical generated inputs to the Python function and the Java program and asserts identical output. |
| `measure_growth(fn, sizes, repeats=5)` | Times `fn` at each size, returns a table with the **ratio between consecutive doublings**, which is the number that identifies the complexity class. |
| `fit_complexity(sizes, times)` | Reports which of O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) best fits, and the residual — so the notebook can say "measured, and it matches" or "measured, and it does not, here is why". |
| `check_invariant(structure, predicate)` | Asserts a structure's invariant holds; used after every operation in a stress test. |
| `edge_cases(kind)` | The standard adversarial inputs for a given input type: empty, size 1, all-equal, already sorted, reverse sorted, all-distinct, many-duplicates, min/max values. |

`dsa_toolkit.py` must itself have no third-party dependencies.

***

## 6. Quality bar — non-negotiables

Rules 1–5 are the DSA-specific core and are stricter than the ML series' equivalents, because in
this domain correctness and cost are *decidable*. Rules 6–12 are inherited and still apply.

1. **Every implementation is differentially tested.** No structure or algorithm ships without a
   randomised stress test against a brute-force reference or the language's built-in, over at
   least 1,000 inputs including every entry from `edge_cases()`. A test that only checks one
   hand-written example does not count.
2. **Python and Java are tested against each other.** Both implementations run on identical
   generated inputs and must produce identical output. This is the DSA analogue of the ML series'
   "implement from scratch and check against scikit-learn in the same cell", and it catches a
   whole class of bug that neither implementation alone would reveal — integer overflow, division
   semantics, sort stability, iteration order.
3. **Every complexity claim is measured.** Time at doubling sizes, print the ratios, and state
   whether the measurement matches the claim. **Where it does not, investigate and write down the
   reason** — constant factors, cache behaviour, interpreter overhead, an input distribution that
   never hits the worst case. A disagreement between theory and stopwatch is the most instructive
   thing a DSA notebook can contain, and it must never be quietly dropped.
4. **Every invariant is asserted in code.** "A heap satisfies the heap property" is a prose claim;
   `check_invariant(h, is_heap)` after every push and pop in a randomised test is a verified one.
   Every structure notebook does the latter.
5. **Every non-obvious algorithm carries its correctness argument.** Greedy gets an exchange
   argument; divide-and-conquer gets its recurrence and Master-theorem case; DP gets its
   optimal-substructure statement; binary search gets its loop invariant. Where a full proof is
   too long, state the argument's shape and cite where the proof lives (CLRS chapter, etc.).
6. **Every code cell must run, in order, under `warnings.simplefilter("error")`.** A warning is a
   failure. Java compiles with `-Xlint:all -Werror`. Run `tools/verify_notebook.py <nb> --run`
   before declaring anything done.
7. **Verify every number in prose against the actual printed output.** Run the cell, read the
   number, *then* write the sentence. Timings especially: never hardcode a measured time in prose
   without re-checking it after the final run, and prefer phrasing that survives a faster machine
   ("roughly 4x per doubling") over a bare millisecond count.
8. **A demo must actually demonstrate its lesson.** If the cell meant to show quicksort's O(n²)
   worst case does not produce it, fix the demo — with a genuinely adversarial input — rather
   than softening the prose. Three demos in the ML series had to be rebuilt for exactly this.
9. **Say what the structure is bad at.** Every notebook has a section on it. A linked list's cache
   behaviour, a trie's memory, a hash table's worst case, DP's state-space blowup.
10. **Never fabricate.** No invented complexities, no invented LeetCode numbers or titles, no
    invented citations or URLs. If a link cannot be fetched and confirmed, mark it
    "search the title" instead of guessing.
11. **No edit-history archaeology.** The reader has one file. State the lesson, not the changelog.
12. **Notebooks ship WITH outputs**, so a reader browsing on GitHub sees the results that back the
    prose. Whatever state a notebook is in it must be internally consistent: a cell with outputs
    carries an `execution_count`. (`verify_notebook.py` enforces consistency, not the choice. The
    ML series ended with nine notebooks lacking stored outputs because this was left to the end —
    **do not repeat that**; save outputs as each notebook lands.)

***

## 7. The canonical template

Same part numbering as the ML series, so a reader can move between the two.

| Part | Content |
|---|---|
| — | Title, "why this notebook is different", contents table, one-paragraph summary |
| **0** | Setup: conditional install cell, one import cell, `dsa_toolkit` import, JDK check |
| **1** | **Theory from zero** — the invariant, the implementation from scratch in **Python**, then in **Java**, cross-checked; the cost, measured; the failure modes |
| **2** | **Worked problems** — 4–6 problems that exercise the structure, solved in full, with the pattern named |
| **3** | **The topic's signature difficulty**, in depth |
| **4** | **Tough questions** — ~12 with `<details>` answers + 3 coding challenges |
| **5** | **Practice problems** — 8–10, ordered by difficulty, each with a brief and the trap it sets |
| **6** | **Reading** — the CLRS/Sedgewick chapters and the papers behind each section |
| — | Appendix: topic-specific errors table, ship checklist, where to go next |

### Conventions that make them feel like one series

- **Python first, then Java, in the same cell where possible** — the Java source as a string
  passed to `run_java`, so both live side by side and the cross-check is one line below them.
  This keeps one notebook and one kernel per topic; no separate Java-kernel notebooks.
- **Every complexity table has a measured column**, not only a claimed one.
- Part 5 problem briefs carry: **what it is / why this one / your brief (numbered) / a good
  result / the trap**.
- Part 4 answers hide in `<details><summary>Answer</summary> … </details>`.
- Prose voice: plain, direct, willing to say an approach is mediocre. No hype.
- Cross-reference other notebooks by section (`NB-09 §1.3`), and link relatively so
  `check_links.py` can verify them.

### Expected scale

The ML series averaged ~52 cells per topic notebook. DSA notebooks carry two languages but
simpler prose, so budget **55–70 cells**, and expect **~1,400 cells** across 23. Do not pad to
hit a number — the shortest ML notebook was the fourth best.

***

## 8. Build & verify workflow

Per notebook, in order. This is the loop the ML series converged on after 16 rounds; do not
shortcut it.

1. **Verify the risky parts first, in scratchpad scripts, before writing a single cell.** Every
   demo that could fail to show its lesson (rule 8) gets proved out first. This is the single
   highest-value habit from the ML build.
2. **Write the notebook as three Python part-files** in the scratchpad — `nbNN_a.py` (front
   matter + Part 0 + Part 1), `nbNN_b.py` (Parts 2–3), `nbNN_c.py` (Parts 4–6 + appendix) — each
   defining `CELLS = []` with `md()` / `code()` helpers.
3. **Build** with `build_nbNN.py`: import the three, assign ids `nbNN-%03d`, `compile()` every
   code cell as a syntax check, write JSON with `indent=1, ensure_ascii=False`.
4. **Run and capture** with `run_nbNN.py`, which executes every code cell with `plt.show` stubbed
   and tees the output to a file.
5. **Audit** every number in the prose against that captured output. Expect to find several
   wrong on the first pass — the ML series averaged two prose corrections per notebook, and the
   best material in it came from investigating those.
6. **Verify** from the repo root (not from the scratchpad — the relative path breaks):
   ```bash
   python tools/verify_notebook.py DSA-Zero-to-Hero/<nb>.ipynb --run --python "<scratch>/venv/Scripts/python.exe"
   ```
7. **Check links:** `python tools/check_links.py`.
8. **Update status:** this file's §3 dashboard, §9 brief and §11 log, plus
   `DSA-Zero-to-Hero/README.md` and the repo root `README.md`.
9. **Save outputs** — open in VSCode, Run All, save (rule 12). Do this now, not at the end of
   the series.

***

## 9. Per-notebook briefs

Each brief is a starting point, not a specification. When a notebook is finished, **replace its
brief with what was actually built**, including the verified headline numbers and anything that
had to be corrected — that record is what makes this file useful to a session with no context.

### NB-00 — Complexity, Amortised Analysis & the Measurement Harness ✅ COMPLETE
54 cells (28 code). Verified: structure clean, all 28 cells run under warnings-as-errors with
Java compiled at `-Xlint:all -Werror`, every printed number audited.

**Builds `dsa_toolkit.py`**, the harness every other notebook imports (§5). It was written and
verified *before* the notebook was drafted against it — the reason NB-00 is built first and alone.
Every function was exercised against a planted failure rather than a happy path: `stress`
minimised an 800-case failure down to `[7]`, and `cross_check` caught a genuine Java `int`
overflow (Python 4,000,000,000 vs Java −294,967,296).

**Headline demonstrations.** These are timings, so they move between machines; the prose states
magnitudes and lets the cells print the figures.

- **The crossover is a real number.** Insertion sort beats merge sort for every n below **100**,
  and by n = 6,400 merge sort is ~70× faster. Both classes confirmed by measurement.
- **Input distribution changes the class.** The same insertion sort measures **O(n²)** on random
  input and **O(n)** on sorted input, where it is ~12× *faster* than merge sort at every size.
- **The language gap.** An identical 20M-addition loop: Python ~3.6 s, Java ~0.009 s, same answer
  — a factor in the hundreds, with JIT compilation and Python's worst-case workload both flagged.
- **Amortised growth, observed rather than timed.** `sys.getsizeof` shows CPython's list settling
  at a growth factor of exactly **1.1251**, with **66 reallocations across 100,000 appends**;
  aggregate cost measures O(n). Replacing geometric growth with grow-by-one measures **O(n²)**.
- **Cache effects are visible from Python.** The same 1,000,000 values summed sequentially, by
  stride 16, and randomly: **1.00× / 1.45× / 2.98×**.
- **Recursion depth.** Python raises `RecursionError` past its 1,000 default; Java survives 5,000
  and reaches `StackOverflowError` around 100,000.
- **A recurrence checked by counting.** Merge sort's comparisons against n·log₂n − n + 1: ratio
  0.96 → 0.98 as n grows. No noise, no constants, machine-independent.
- **The Master theorem's three cases, counted per level** at n = 1024: total/n = 2.00,
  total/(n log n) = 1.10, total/n² = 2.00 respectively.

**Three demos were corrected against their own output**, per quality-bar rules 2 and 3:

1. **A bug in my own verification code.** `random.Random(n).randrange(...)` inside a comprehension
   re-seeds per element and yields a list of **identical values** — insertion sort's best case.
   That made an O(n²) algorithm measure as O(n), and produced a first draft in which insertion
   sort won at every size up to 6,400. The fix is one shared generator, and the bug was
   instructive enough to become **§3.1**, which now reproduces it deliberately as "the benchmark
   that measures the wrong distribution".
2. **The amortised demo measured noise.** Timing individual appends gave 93 scattered spikes with
   no geometric pattern — allocator and OS noise swamp it. Replaced with `sys.getsizeof`, which
   observes capacity directly: exact, reproducible, and a much clearer picture.
3. **§3.2's headline was a single unstable draw.** I wrote that a narrow-range fit reports O(n)
   for merge sort; re-run, it reported O(n log n). Measured across 8 repetitions the verdict
   **flips — 5× O(n log n), 3× O(n)** — while the wide range is 4/4 stable. §3.2 is therefore now
   about **reproducibility** rather than a wrong answer, which is both more honest and the more
   useful lesson: one convincing run is not evidence. The section still proves the fitter is not
   at fault, by feeding it noise-free data where it separates the classes exactly.

**Tooling change this required.** `tools/verify_notebook.py` extracted cells into a script in the
system temp directory and ran it there, so `from dsa_toolkit import ...` failed even though it
works in Jupyter. Fixed twice over: run with `cwd` set to the notebook's directory, **and** put
that directory on `sys.path` in the generated runner — because for `python script.py`,
`sys.path[0]` is the script's directory, not the working directory. The first fix alone was not
enough. Regression-checked against an ML notebook.

**(original brief follows)**

- **Unique theory:** Big-O/Ω/Θ and what each is *for*; why constants matter in practice; the RAM
  cost model and where it lies (cache, branch prediction); **amortised analysis** by all three
  methods (aggregate, accounting, potential); recurrences and the Master theorem; space
  complexity including recursion stack.
- **Must cover:** how to *measure* a complexity class rather than assert it — the doubling
  experiment and how to read the ratio; why a single timing is meaningless; warm-up and GC noise.
- **Builds:** `dsa_toolkit.py` (§5), from scratch, explained. This is the notebook's Part 2.
- **The signature difficulty (Part 3):** cases where the measurement disagrees with the bound —
  an O(n²) that beats an O(n log n) at realistic sizes, cache effects making a "worse" layout
  faster, Python's constant factor versus Java's.
- **Java angle:** JIT warm-up, why the first run is a lie, and how `run_java` handles it.
- **Reading:** CLRS ch. 2–4, 17. Bentley, *Programming Pearls*.

### NB-01 — Arrays & Dynamic Arrays ✅ COMPLETE
43 cells (21 code). Verified: structure clean, all 21 cells run under warnings-as-errors with
Java compiled at `-Xlint:all -Werror`, every printed number audited.

**Structure as built:** Part 1 theory (contiguity and the address formula · what contiguity costs
· **the dynamic array from scratch, cross-checked against Java** · **memory: pointers, machine
ints and the boxing tax**) → Part 2 the techniques that *fall out of* contiguity (prefix sums ·
difference arrays · two pointers · sliding window · the quadratic accident) → **Part 3 cache
locality** → Part 4 questions → Part 5 practice → Part 6 reading.

**Headline demonstrations.** These are timings and move between machines, so the prose states
magnitudes and lets the cells print the figures:

- **The growth factor is a priced decision.** Sweeping it over 100,000 appends: 1.125x copies
  **8.24 elements per append** and wastes 2.9%; 2.0x copies **1.31** and wastes 31.1%; 4.0x copies
  **0.87** and holds **162.1% more memory than it needs**. Every row is amortised O(1) — the
  constant is what you are choosing.
- **Memory and speed pull in opposite directions.** A list of 2,000,000 ints costs **36.0
  bytes/element**; `array.array('i')` costs **4.2** — an **8.5x** saving — and is **2.6x SLOWER**
  to sum, because every access boxes a machine int into a Python object. Stated as a trade, not a
  win.
- **Java's boxing tax:** `Integer[]` sums close to **3x** slower than `int[]`, and costs ~6x the
  memory.
- **Cache locality is the signature result.** Same Java array, same operation count, only the loop
  order differs: **8.4x** at 4000x4000.
- **AoS vs SoA:** reading one field of 20,000,000 records is **~2.4x** slower from `Particle[]`
  than from a parallel `double[]`.
- **Difference arrays:** **over 400x** faster than the naive version at 400 range updates, and
  flat in the number of updates where naive is linear.
- **The quadratic accident:** `list.insert(0, x)` in a loop measures a clean **O(n^2)**, and the
  linear alternative is still faster in absolute terms at eighty times the size.
- **`System.arraycopy`** is about **20x** faster than a hand-written copy loop at n=1,000 and
  roughly a **wash at 20,000,000**, where both are memory-bandwidth-bound. The honest version of
  "intrinsics are faster".
- **Cross-language:** the Python and Java dynamic arrays agree exactly on (resizes, elements
  copied, final capacity) across 25 random sizes — so the amortised argument verified on one
  transfers to the other.

**Four demos were corrected against their own output**, per quality-bar rules 2 and 3:

1. **AoS vs SoA does not work in Python.** It measured 1.15x, because a list of objects and a list
   of ints are *both* pointer arrays — there is no locality difference to find. Moved to Java,
   where objects genuinely live elsewhere, and it shows ~2.4x.
2. **My memory comparison was meaningless as first written.** `getsizeof(list)` against
   `getsizeof(array.array)` reported 8.23 vs 8.24 bytes/element — an 8.5x difference measured as
   none — because it counts the pointer array and omits the int objects. Fixed to deep-size the
   list, and the notebook now warns about exactly this.
3. **"The complexity actually differs" for prefix/difference arrays was wrong.** With the update
   count held fixed, naive is O(u*n) and difference is O(u+n), and *both* are linear in n. Fixed by
   sweeping u instead, which shows naive linear and difference flat.
4. **The cache penalty is not monotonic in array size.** Measured 1.82x at 1000², **1.11x at
   2000²**, 8.43x at 4000². The middle array is still substantially cache-resident on this
   machine, so §3.1 now says the cliff is a property of the machine rather than a smooth trend,
   and points at Practice 7.

**A fifth correction, and it is NB-00 §3.2 recurring.** Three cells claimed O(n) and the fitter
reported O(n log n): the dynamic-array append sweep, the naive range-update sweep, and the linear
half of the quadratic-accident demo. All three are genuinely linear; at these sizes the two
classes are within noise. Rather than inflate the sizes until the notebook is slow, the claims
were dropped and the prose now tells the reader to read the **ratio** column and explains why the
label is unreliable here. That is the third notebook in which this has come up, which is itself
worth knowing.

**(original brief follows)**

- **Unique theory:** contiguous memory and O(1) indexing; the growth-factor argument and
  **amortised O(1) append proved three ways**; why 2x (Java `ArrayList`) versus ~1.125x (CPython
  `list`) and what that trades; insert/delete in the middle.
- **Must cover:** prefix sums and difference arrays; two pointers; sliding window — all derived
  as consequences of contiguity rather than presented as tricks.
- **Signature difficulty:** cache locality. Measure array-of-structs vs struct-of-arrays, and
  row-major vs column-major traversal of a 2-D array; the ratio is large and surprising.
- **Java angle:** `int[]` vs `Integer[]` boxing, `ArrayList` internals, `System.arraycopy`.
- **Bad at:** insertion, unknown final size, sparse data.

### NB-02 — Strings & String Algorithms ✅
**39 cells (18 code, 21 markdown). Structure clean; all 18 cells run under warnings-as-errors;
Java compiled at `-Xlint:all -Werror`; every number audited against printed output.**

- **Unique theory:** immutability and its consequences; the concatenation trap measured on **two
  axes**; string builders; encodings and why `len()` cannot mean what people want it to.
- **Covered:** naive matching, KMP with the prefix function derived and its amortised proof,
  Z-algorithm, Rabin-Karp with the rolling hash and the verification step.
- **Signature difficulty (§3):** why naive matching survives in practice, measured rather than
  asserted.
- **Java angle:** `String +=` vs `StringBuilder`, UTF-16 `length()` vs `codePointCount`, the
  interning pool and why `==` is a bug that passes its tests.

**The finding that made the notebook.** The `s += chunk` optimisation fails on *two* independent
axes, and only one of them is folklore:

| Regime | Fit | Relative error |
|---|---|---|
| `+=`, refcount 1, result **50 KB → 400 KB** | **O(n)** | 0.005 |
| `+=`, refcount 1, result **2 MB → 16 MB** | **O(n²)** | 0.02 |
| `+=`, one extra reference held, any size | **O(n²)** | 0.06 |
| `"".join(parts)`, timed alone | **O(n)** | 0.005 |

The **size cliff** was not planned. It was found because the original 20k–160k table produced a
reproducible 5× ratio in its last row instead of the expected 2×, and again — more subtly — when
the linear table's 800 KB row drifted to 2.5. The linear range now stops at a 400 KB result for
that reason, and the notebook says so rather than hiding it. `realloc` cannot extend a
multi-megabyte block in place, so the quadratic returns with no second reference anywhere. The
same function is exactly linear and exactly quadratic depending only on how much you build.

**A methodology error caught in the same section.** `''.join(parts)` measured as O(n log n) and the
harness rejected the O(n) claim — correctly, because the timed function *included the loop that
filled the list*. Timing the join alone via `setup=` gives O(n) with relative error 0.005. The
lesson is now in the notebook: measure the thing you are claiming about, not the thing wrapped
around it.

**Verified numbers cited in prose:**
- Naive comparisons per character of text: random binary **2.00**, English-like **1.00**,
  adversarial **498.50**. The realistic figures do not depend on pattern length; the adversarial
  one does.
- Naive **O(n²)** (err 0.10) vs KMP **O(n)** on the same adversarial family; head-to-head speed-up
  **~330× at 8,000, ~670× at 16,000, ~1,250× at 32,000** — growing, hence a complexity difference.
- Java `String +=` vs `StringBuilder`: **~76× / ~153× / ~319×** at n = 10k/20k/40k. Timing-derived
  figures like these are quoted as ranges in the notebook's prose, never as exact values.
- Unicode `len()` / UTF-8 bytes / UTF-16 units — ascii 4/4/4; precomposed é 4/5/4; decomposed
  5/6/5; G clef **1**/4/**2**; family emoji **5**/18/**8**; flag 2/8/4.
- Java: `clef.length()=2 codePointCount=1`; precomposed vs decomposed `equals=false`;
  `a==b true | a==c false | a==c.intern() true`.
- Rabin-Karp false positives searching 20,000 chars of a–h for `"hello!"` (which cannot occur):
  mod 101 → **195**, mod 1009 → **20**, mod 100003 → 0, mod 2⁶¹−1 → 0. **Without the verification
  step, mod 101 reports 195 matches for a pattern that never occurs.**
- Differential testing: naive 5,009 cases; prefix_function 4,007; KMP 6,009; z_function 5,006;
  Z-search 5,009; Rabin-Karp 4,009 — all agree with brute force.

- **Bad at:** Unicode-correct operations, which almost every implementation gets wrong.

### NB-03 — Hashing & Hash Tables ✅
**58 cells (23 code, 35 markdown). Structure clean; all 23 cells run under warnings-as-errors;
Java at `-Xlint:all -Werror`; every number audited against printed output.**

- **Unique theory:** what a hash function must guarantee (uniformity measured with a $\chi^2$
  test); collisions as the birthday bound; **chaining and open addressing both built from
  scratch**; load factor measured against Knuth's formulas.
- **Covered:** the canonical-key, complement-lookup, prefix-sums-in-a-map and membership-set
  patterns as Part 2 applications, each with its named reframing.
- **Signature difficulty (§3):** the adversarial input, in full. Constructs colliding keys for
  both Java's `String.hashCode` and CPython's `int` hash, measures CPython's `dict` going
  quadratic, and shows each language defends the axis the other leaves open.
- **Java angle:** the `hashCode`/`equals` contract (all three violations measured), treeification,
  and mutable keys — with `javac` itself catching the missing-`hashCode` bug under `-Werror`.

**The findings that shaped it:**

| Measurement | Result |
|---|---|
| Four hash functions, $\chi^2/df$ (target 1.0) | first-char **766**, sum-of-chars **51**, poly-31 **0.97**, Python **~1.0** |
| First collision into 4,096 buckets | **~80 keys** (birthday bound $\sqrt{\pi m/2}$), matched to 3% |
| Linear probing at $\alpha=0.95$ | **~180 probes** vs chaining's **~1**, matching $\frac12(1+(1-\alpha)^{-2})$ |
| Chaining at $\alpha=8$ | **8.0 probes**, ratio to theory 0.999 |
| CPython `dict`, colliding int keys | **$O(n^2)$**, thousands× slower at n=16k, quadrupling per doubling |
| Same colliding-string family, Python vs Java | Python **~1.0×** (SipHash), Java **~10×** flat (treeification) |

- **The open-addressing delete bug is caught by the stress test**, minimised to three operations
  (`put -10, put 14, del -10` → "live key 14 not reachable"). The buggy version keeps its counters
  consistent, so only the *reachability* invariant catches it — a structural invariant, not a
  numeric one.
- **The `hashCode`/`equals` contract violation is caught by `javac` itself.** `-Xlint:all -Werror`
  refuses to compile a class that overrides `equals` without `hashCode`; you have to
  `@SuppressWarnings` to demonstrate the runtime damage. The compiler flag is worth more than the
  knowledge.
- **Two measurement confounds caught during the audit, both mine.** (1) The two-sum O(n) timing
  wandered between O(n) and O(n log n) run-to-run; switched to counting elements examined (exactly
  2.00 per doubling) per NB-00 §1.7. (2) The "Python is immune to the Java collision family" cell
  first showed a spurious 10× because it timed string *construction*; fixed by building keys in
  `setup` and comparing against same-length control keys, giving the true ~1.0×.

- **Bad at:** ordering, range queries, worst-case guarantees, memory overhead.

### NB-04 — Linked Lists ✅
**56 cells (21 code, 35 markdown). Structure clean; all 21 cells run under warnings-as-errors;
Java at `-Xlint:all -Werror`; every number audited against printed output.**

- **Unique theory:** node layout and per-element cost measured; singly and doubly linked lists
  built from scratch with invariants asserted after every operation; **sentinel nodes** with the
  branch saving *counted in bytecode*.
- **Covered:** reversal (iterative and recursive, with the recursion limit measured), **Floyd's
  cycle detection with the proof**, merge-by-splicing with a stability check, and the LRU cache.
- **Signature difficulty (§3):** linked lists are usually the wrong answer — traversal, indexing,
  and the workloads where they genuinely win, ending in a three-condition decision rule.
- **Java angle:** `int[]` vs `ArrayList` vs `LinkedList` benchmarked; `ArrayDeque` beating
  `LinkedList` at queueing; why the JDK discourages it.

**Headline measurements** (timings move between machines, so the prose states shapes and ranges):

| Measurement | Result |
|---|---|
| Per-element memory | list slot **8 B**, node with `__slots__` **48 B**, without **136 B**, doubly **56 B** |
| Node address gap, allocated in link order | **48 bytes** — exactly one node, packed adjacent |
| Python traversal, scattered vs in-order nodes | **2.3×**, identical structure, layout alone |
| Java sum of 1M: `int[]` / `ArrayList` / `LinkedList` | 1× / **~9×** / **~30×** |
| Java `get(i)`, 20k random reads | `ArrayList` <1 ms, `LinkedList` **>1 s — 1,400×** |
| Bulk removal via iterator (Java) | LinkedList wins **9× → 55× → 247×**, growing |
| Delete-every-other, counted (Python) | linked **n writes** vs array **~n²/4 moves**; ratio 2,500× → 20,000× |
| Sentinel branch count (bytecode) | **7 vs 3** total, **4 vs 0** structural, `unlink` **2 vs 0** |
| Recursive reversal | fails at **n = 1,000**; iterative does 2,000,000 in 0.16 s |

**Two predictions were wrong and the measurements were kept:**

- **A 2-and-4 walker does not miss cycles.** I claimed it fails on odd-length cycles; testing 820
  cycles × 6 step-pairs found **zero** detection failures for any pair. Once both pointers are in
  the cycle, $(b-a)k \equiv 0 \pmod c$ holds at $k=c$ for *any* unequal speeds. What actually
  breaks is the **entry-finding phase**: (1,3), (3,5) and (1,4) reported the wrong entry on 253,
  306 and 205 of 820 cycles, while (1,2), (2,4) and (2,3) were always right — the pattern is
  exactly whether $(b-a)$ divides $a$. The section now teaches that instead, which is a better
  point than the one I planned.
- **Scattering nodes does not slow Java down.** Two attempts (ballast between allocations, two
  interleaved lists) both made traversal *faster* (0.63×, 0.73×). The JVM's compacting collector
  relocates live objects in reference order, so the scattering does not survive to be measured.
  CPython never moves objects, which is why the same experiment gives a clean 2.3× there. The
  Java scattered row was removed from the main table and the finding became its own cell.

- **Bad at:** indexing, locality, memory per element.

### NB-05 — Stacks, Queues & Deques ✅
**50 cells (18 code, 32 markdown). Structure clean; all 18 cells run under warnings-as-errors;
Java at `-Xlint:all -Werror`; every number audited against printed output.**

- **Unique theory:** LIFO/FIFO as invariants; the **circular buffer** built from scratch and
  verified against `collections.deque`; the **two-stack queue** with its amortised bound counted
  rather than asserted.
- **Covered:** the **monotonic stack derived from its invariant**, then applied four ways — next
  greater element, daily temperatures, largest rectangle in a histogram, and sliding window maximum
  (the monotonic **deque**).
- **Signature difficulty (§3):** the invariant nobody writes down — stated, asserted inside the
  loop, and used to prove the linear bound by counting.
- **Java angle:** `Stack` vs `ArrayDeque` — with the usual performance argument **measured and
  found wrong**.

**Headline measurements:**

| Measurement | Result |
|---|---|
| `list.pop(0)` queue vs `deque` | O(n²) vs O(n); ratio **13× → 24× → 47× → 91×**, doubling |
| `RingDeque` (ours, pure Python) | **O(n)**, err 0.008; beats `list` from n≈20k, ratio doubling |
| Two-stack queue, amortised | **exactly 2.00 movements/op** at n = 1k…1M |
| Two-stack queue, worst single op | **200,001 movements**, next op **1** |
| Monotonic stack, total work | **≤ 2 ops/element always**: increasing 2.00, decreasing 1.00, all-equal 1.00 |
| Brute force vs stack, **decreasing** input | brute **O(n²)** (err 0.011), stack O(n), 1.00 ops/elem |
| Brute force vs stack, **increasing** input | brute **O(n)** (err 0.029) — same class as the stack |

**Three findings worth carrying forward:**

- **The invariant assertion caught the notebook's own prose.** §3.1's first draft asserted the
  monotonic stack is *strictly decreasing*; the assertion failed on `[0, 0]` within seconds, because
  popping on `<` never evicts an equal value. The correct invariant is **non-increasing**. This is
  now the section's opening argument for writing invariants as code.
- **The two bug demos are caught by different tools, and neither catches both.** `if` instead of
  `while` breaks the structure and the **invariant** fires on a 3-element input; `<=` instead of
  `<` leaves a perfectly well-formed monotonic stack answering a different question, and only the
  **differential test** catches it. Complements NB-04 §1.4, where the reachability invariant was
  the only thing that fired.
- **The "monotonic stack turns O(n²) into O(n)" framing is wrong for half of all inputs.** The two
  algorithms have *opposite* worst cases: on decreasing input brute force is O(n²) and the stack
  pops nothing; on increasing input brute force is **O(n)** — the same class as the stack — while
  the stack does its maximum. The honest claim is that the stack's cost is **bounded regardless of
  input** while the brute force's is **a property of the data**, which is the NB-02 §3 / NB-03 §3
  theme arriving a third time.

- **Bad at:** random access, searching.

### NB-06 — Trees & Traversals ⬜
- **Unique theory:** the recursive definition and why it makes recursion the natural tool; the
  four traversals; the **explicit-stack conversion** for each; **Morris traversal** for O(1) space.
- **Must cover:** height/depth/diameter; level order with BFS; recursion → iteration.
- **Signature difficulty:** **Python's recursion limit is a real constraint.** Build a degenerate
  10,000-node tree, hit `RecursionError`, then fix it with an explicit stack — and compare against
  Java's stack depth on the same input.
- **Java angle:** default thread stack size, `-Xss`, `StackOverflowError`.
- **Bad at:** anything needing an ordering guarantee without the BST invariant (NB-07).

### NB-07 — Binary Search Trees ⬜
- **Unique theory:** the BST invariant stated precisely (not "left is smaller"); search, insert
  and the three delete cases; inorder traversal yields sorted order, and why that is the invariant
  restated.
- **Must cover:** validate-BST done correctly (the range argument, not the parent comparison);
  successor/predecessor; LCA.
- **Signature difficulty:** **degeneration.** Insert sorted data and measure the tree become a
  linked list — O(log n) → O(n), demonstrated, which is the entire motivation for NB-08.
- **Java angle:** `Comparable`/`Comparator`, and why `TreeMap` exists.
- **Bad at:** adversarial or sorted insertion order; nothing guarantees balance.

### NB-08 — Balanced Trees & B-Trees ⬜
- **Unique theory:** the **second invariant** layered on the BST one; **AVL** with all four
  rotations implemented and the height bound derived; **red-black** properties and why its looser
  balance means fewer rotations; **B-trees** and the disk/page argument.
- **Must cover:** rotations as the universal repair primitive; when each is preferred.
- **Signature difficulty:** rotation code is where everyone gets it wrong. Every rotation is
  followed by `check_invariant` in a randomised stress test of 10,000 mixed operations.
- **Java angle:** `TreeMap`/`TreeSet` are red-black; measure against `HashMap` to show what
  ordering costs.
- **Bad at:** the constant factor versus a hash table when ordering is not needed.
- **Note:** red-black insertion/deletion in full is long. Implement AVL completely; do red-black
  at the properties-and-consequences level and say so plainly.

### NB-09 — Heaps & Priority Queues ⬜
- **Unique theory:** the heap property as an invariant; the implicit array layout; sift-up and
  sift-down; **heapify in O(n)**, with the summation proof and then the measurement confirming it
  against the naive O(n log n) build.
- **Must cover:** top-k, running median with two heaps, k-way merge, heapsort; d-ary heaps and the
  cache argument; **indexed heaps for decrease-key**, which Dijkstra (NB-21) needs.
- **Signature difficulty:** a heap is not sorted, and the array is not a sorted array — the most
  common misconception; demonstrate directly.
- **Java angle:** `PriorityQueue` is a binary heap; it has no decrease-key, and what people do
  instead (lazy deletion) — measured.
- **Bad at:** search, arbitrary deletion, iteration in order.

### NB-10 — Tries ⬜
- **Unique theory:** the prefix tree; time is O(length) and **independent of the number of keys**,
  which is the whole point; node representation trade-offs (array vs map children).
- **Must cover:** insert/search/prefix-search/delete; autocomplete; word-search-on-grid with a trie.
- **Signature difficulty:** **memory.** Measure a trie against a `set` for the same word list;
  the overhead is large. Then compress it (radix tree) and measure again.
- **Java angle:** `HashMap<Character, Node>` vs `Node[26]`, and the boxing cost.
- **Bad at:** memory, non-prefix queries, large alphabets.

### NB-11 — Disjoint Set Union ⬜
- **Unique theory:** the forest representation; **union by rank/size** and **path compression**
  separately, then together; the α(n) inverse-Ackermann bound and what it means in practice.
- **Must cover:** connected components, cycle detection in undirected graphs, Kruskal's inner loop
  (feeding NB-21).
- **Signature difficulty:** measure all four combinations (neither optimisation, each alone, both)
  on a million operations. The gap is dramatic and makes the theory concrete.
- **Java angle:** straightforward; use it to show a clean `int[]`-backed implementation with no
  object overhead.
- **Bad at:** deletion, splitting, any query other than "same set?".

### NB-12 — Fenwick & Segment Trees ⬜
- **Unique theory:** prefix sums as the O(1)-query/O(n)-update extreme; **Fenwick tree** and the
  low-bit trick derived, not stated; **segment tree** as the general form; **lazy propagation**.
- **Must cover:** point update + range query, range update + point query, range update + range
  query; which structure each calls for.
- **Signature difficulty:** the index arithmetic. Every operation is stress-tested against a naive
  O(n) reference over randomised operation sequences — this is the notebook where rule 1 earns its
  keep.
- **Java angle:** direct; a good place to show the memory difference between the two structures.
- **Bad at:** non-invertible operations for Fenwick (min/max need a segment tree); dynamic sizes.

### NB-13 — Sorting I: Comparison Sorts & the Lower Bound ⬜
- **Unique theory:** insertion, selection, bubble, merge, quick, heap — all implemented; the
  **decision-tree Ω(n log n) lower bound**, proved; **stability** defined and demonstrated;
  in-place vs not.
- **Must cover:** quicksort's pivot problem and the adversarial input that forces O(n²); why
  randomised pivots fix it in expectation.
- **Signature difficulty:** **what the built-ins actually do.** CPython's Timsort and Java's
  dual-pivot quicksort / Timsort split — measure all of them against the hand-written versions on
  random, sorted, reverse and nearly-sorted input. The nearly-sorted column is where Timsort's
  design shows.
- **Java angle:** `Arrays.sort` is dual-pivot quicksort for primitives and Timsort for objects —
  and **why** that difference exists (stability matters for objects, not for ints).
- **Bad at:** the lower bound is the point — no comparison sort escapes it, which sets up NB-14.

### NB-14 — Sorting II: Linear-Time Sorts & Selection ⬜
- **Unique theory:** how counting, radix and bucket sort **escape the comparison model** by
  assuming something about the keys; the assumptions stated precisely and the cost of violating
  them measured.
- **Must cover:** **quickselect** and its expected O(n); **median of medians** for worst-case O(n),
  implemented, and then measured to show its constant factor makes it lose in practice — an honest
  result worth stating.
- **Signature difficulty:** radix sort's k factor. Its "O(n)" hides O(nk); find the key range where
  it actually beats Timsort, and be explicit that it is narrower than the folklore suggests.
- **Java angle:** primitive arrays make counting sort genuinely fast; show it.
- **Bad at:** large or unbounded key ranges, memory.

### NB-15 — Binary Search & the Invariant Discipline ⬜
- **Unique theory:** the loop invariant written out, and **every off-by-one derived from it**
  rather than memorised; `lo < hi` vs `lo <= hi`; the four boundary variants; `lower_bound` /
  `upper_bound`.
- **Must cover:** **binary search on the answer** — the pattern that turns an optimisation problem
  into a predicate; rotated arrays; 2-D matrices; real-valued search and the termination condition.
- **Signature difficulty:** the classic overflow bug `(lo + hi) / 2` — which **Java actually
  exhibits and Python does not**, making it the single best demonstration of why the series is
  bilingual. Show `Arrays.binarySearch`'s history (the JDK carried this bug for nine years).
- **Java angle:** as above, plus `>>> 1` as the fix.
- **Bad at:** unsorted data, and predicates that are not monotone — demonstrate a wrong answer.

### NB-16 — Recursion & Divide and Conquer ⬜
- **Unique theory:** base case / recursive case / progress; the call stack made concrete;
  **recurrences and the Master theorem** applied to merge sort, binary search, Karatsuba;
  tail calls and why Python does not eliminate them.
- **Must cover:** memoisation as the bridge to NB-19; converting recursion to iteration; when
  recursion is genuinely clearer.
- **Signature difficulty:** stack depth and its cost. Measure recursive vs iterative Fibonacci,
  factorial and tree traversal in both languages; show `sys.setrecursionlimit` is a loaded gun.
- **Java angle:** `StackOverflowError`, `-Xss`, and the absence of TCO there too.
- **Bad at:** deep recursion, and problems with heavy overlapping subproblems (→ NB-19).

### NB-17 — Backtracking ⬜
- **Unique theory:** the state-space tree; **choose / explore / unchoose** as an invariant about
  restoring state; why the unchoose step is where bugs live; **pruning** as the difference between
  usable and useless.
- **Must cover:** subsets, permutations, combinations (and the duplicate-handling that each needs);
  N-Queens; Sudoku; word search.
- **Signature difficulty:** measure the search tree with and without pruning — node counts, not
  just times. N-Queens at n=8 with and without the diagonal check is a factor of thousands.
- **Java angle:** passing mutable state, `char[][]` boards, and why deep-copying instead of
  undoing is the common performance mistake.
- **Bad at:** anything where the state space is genuinely exponential and pruning does not bite.

### NB-18 — Greedy Algorithms & Exchange Arguments ⬜
- **Unique theory:** the greedy-choice property and optimal substructure; **the exchange argument
  as a proof technique**, worked in full for interval scheduling; matroids named as the general
  theory with a pointer, not developed.
- **Must cover:** activity selection, interval merging, Huffman coding (implemented, and its
  optimality argued), jump game, fractional knapsack.
- **Signature difficulty:** **when greedy fails.** 0/1 knapsack with a counterexample constructed
  and verified by brute force; coin change where greedy fails for a specific coin system, found by
  search rather than asserted. This is the section that teaches the topic.
- **Java angle:** `Comparator` composition for the sort that most greedy algorithms start with.
- **Bad at:** anything without the greedy-choice property — and you must prove it has one.

### NB-19 — Dynamic Programming ⬜
- **Unique theory:** optimal substructure and overlapping subproblems, both stated precisely;
  memoisation vs tabulation; **state design as the actual skill**; transition; base cases;
  space optimisation by keeping only the needed rows.
- **Must cover:** 1-D (climbing stairs, house robber, coin change), 2-D (LCS, edit distance,
  knapsack), LIS in both O(n²) and O(n log n), DP on trees, DP on DAGs, bitmask DP.
- **Signature difficulty:** **finding the state.** Take one problem and work through three
  candidate state definitions, showing two of them fail — the reasoning that is normally left out.
- **Java angle:** `int[][]` vs `HashMap` memo tables, measured; `Integer` boxing in memo maps.
- **Bad at:** state-space blowup; problems where the state is not finite or not small.
- **Note:** the largest notebook in the series. If it exceeds ~80 cells, split into 19a
  (foundations + 1-D/2-D) and 19b (trees, DAGs, bitmask) and update §3.

### NB-20 — Graphs I: Representation & Traversal ⬜
- **Unique theory:** adjacency list vs matrix vs edge list, with the density crossover **measured**;
  directed/undirected, weighted/unweighted; BFS and DFS with their invariants; the visited set as
  a termination argument.
- **Must cover:** connected components; cycle detection (and why the directed and undirected cases
  need different algorithms); bipartite checking; **topological sort** by both Kahn and DFS;
  grid problems as implicit graphs; multi-source BFS.
- **Signature difficulty:** modelling — recognising a problem as a graph problem. Several
  non-obvious framings worked through (word ladder, course schedule, islands).
- **Java angle:** `List<List<Integer>>` vs `int[][]`; the boxing cost, measured.
- **Bad at:** dense graphs with a list representation, and vice versa — hence the crossover.

### NB-21 — Graphs II: Shortest Paths, MST & Flow ⬜
- **Unique theory:** BFS for unweighted; **Dijkstra with its greedy-choice proof** and why negative
  edges break it — demonstrated, not asserted; **Bellman-Ford** and negative-cycle detection;
  **Floyd-Warshall** as DP on graphs; A* and admissible heuristics; **Prim and Kruskal** with the
  cut property; max-flow/min-cut at a concept level with Ford-Fulkerson implemented.
- **Must cover:** which algorithm for which graph — the decision table, justified.
- **Signature difficulty:** Dijkstra with a `PriorityQueue` that has no decrease-key. Implement
  both lazy deletion and an indexed heap (NB-09) and measure the difference on a large sparse graph.
- **Java angle:** `PriorityQueue<int[]>` versus a custom comparator; the lazy-deletion idiom.
- **Bad at:** negative weights (Dijkstra), dense graphs (Bellman-Ford), memory (Floyd-Warshall).

### NB-22 — Bit Manipulation ⬜
- **Unique theory:** two's complement; AND/OR/XOR/NOT/shifts; **XOR's group structure** and why it
  makes the single-number problems work; masks; `n & (n-1)` and the other identities, derived.
- **Must cover:** counting bits (naive, Kernighan, table, popcount), subset enumeration via
  bitmasks (feeding NB-19), swapping without a temp and why it is a bad idea in practice.
- **Signature difficulty:** **Python has arbitrary-precision integers and Java does not.** This is
  the notebook where the two languages differ most: Java's `int` overflow, `>>` vs `>>>`, and
  Python's infinite sign extension all produce different answers to the same expression. Show them
  disagreeing, then show how to write Python that emulates 32-bit behaviour.
- **Java angle:** the whole notebook, effectively; `Integer.bitCount`, `Long`, the shift operators.
- **Bad at:** readability. Say so — most bit tricks belong in a library, not in your code.

***

## 10. Open questions and decisions

- [x] ~~**Install a JDK**~~ — done 2026-09-07: **Temurin 21.0.12** at
      `C:\Program Files\Eclipse Adoptium\jdk-21.0.12.101-hotspot`, via
      `winget install --id EclipseAdoptium.Temurin.21.JDK -e`. It is **not on PATH**;
      `dsa_toolkit` finds it by searching the standard install roots, so no PATH change is
      needed and none was made.
- [x] **Language** — Python and Java side by side. Decided 2026-09-07 by the owner.
- [x] **Granularity** — finer-grained; 23 notebooks (§3). Decided 2026-09-07.
- [x] **Emphasis** — foundations first (§1). Decided 2026-09-07.
- [x] ~~**Java-in-notebook mechanism.**~~ Settled, and proven by NB-00: Python cells hand Java
      source to `run_java()`; one notebook and one kernel per topic; `verify_notebook.py`
      works unchanged. Both languages sit in the same cell, which is what makes §2.3's
      cross-language check readable at all. **Cost measured: ~0.12 s of JVM start-up per
      call**, so `cross_check` is an n≈50 tool and anything needing thousands of cases must
      batch them into one JVM run. NB-15 and NB-22 will need that.
- [x] ~~**Repo root README DSA section**~~ — the folder is listed, and now that NB-00 exists
      `DSA-Zero-to-Hero/README.md` is the reader-facing guide it points at.
- [ ] **A `PROBLEM_LOG.md`** in this folder, modelled on tracker 2's problem log — worth it once
      three or four notebooks exist and there is something to log.
- [ ] **Practice problems (Part 5): where do they come from?** They must be real and correctly
      titled (rule 10). Proposed: name the problem and its source (LeetCode title, not number —
      numbers change), and never invent one.
- [x] ~~`verify_notebook.py`'s stale docstring reference~~ — fixed while making the tool run
      notebooks from their own directory (see the NB-00 log entry).

***

## 11. Status log

Append a dated entry every session. Newest first.

### 2026-09-08 (NB-05)
- **NB-05 Stacks, Queues & Deques: COMPLETE.** 50 cells (18 code, 32 markdown). Structure clean,
  all 18 cells run under warnings-as-errors, Java at `-Xlint:all -Werror`, every number audited.
  **6 of 23.**
- **An invariant assertion caught my own prose, which is the best possible advertisement for the
  practice.** I wrote that a monotonic stack is "strictly decreasing"; asserting it failed on
  `[0, 0]` in seconds, because popping on `<` never evicts an equal value. The correct statement is
  **non-increasing**. That correction now opens §3.1 rather than being quietly fixed, because the
  point of the section is precisely that a comment saying "strictly decreasing" is wrong forever
  and silently while an assertion is wrong once and loudly.
- **The two-bug demo in §3.1 is the sharpest tool-coverage illustration in the series so far.**
  `if` instead of `while` breaks the structure, so the invariant fires on a three-element input;
  `<=` instead of `<` leaves a perfectly well-formed monotonic stack answering a different
  question, and only the differential test catches it. Together with NB-04 §1.4 (where only the
  reachability invariant fired) the series now has both directions demonstrated: invariants and
  reference implementations catch disjoint bug classes, and you need both.
- **The signature difficulty came out inverted from the brief, again, and better for it.** The
  brief framed monotonic stacks as O(n²)→O(n). Measuring both algorithms on both extremes shows
  they have *opposite* worst cases: on increasing input the brute force is O(n), the same class as
  the stack. The honest claim is about a **bounded** cost versus a **data-dependent** one, which is
  the same lesson as NB-02 §3 (naive matching) and NB-03 §3 (hash flooding) reached a third way.
  Three notebooks converging on "who chooses the input?" is now a deliberate through-line.
- **A widely repeated Java claim did not survive measurement.** `Stack` being slow because
  `Vector` is synchronized is folklore: across three trials at two sizes with heavy JIT warm-up the
  ratio bounced either side of 1.0. Modern JITs optimise uncontended locks. The case against
  `Stack` is entirely its API — `get(0)`, `insertElementAt` into the middle, `removeElementAt(0)`,
  and a `toString` that prints the reverse of pop order — and the notebook makes that case instead.
  This is the third measured correction to received wisdom (after NB-04's two).
- **Measurement hygiene:** the §3.3 growth tables needed different size ranges per algorithm (1k–8k
  for the quadratic brute force, 100k–800k for the stack, which is too fast to time below that).
  Stated in the output rather than silently chosen.
- **Stored outputs and hygiene:** 31 outputs via nbclient, no stderr, no leaked paths, no bare
  `---` hrules, Quarto renders, structure re-verified.
- **Next:** NB-06 Trees & Traversals — where §1.1's stack-for-depth / queue-for-breadth observation
  becomes DFS and BFS, and Q9's "any recursion can be made iterative with an explicit stack" gets
  built.

### 2026-09-08 (NB-04)
- **NB-04 Linked Lists: COMPLETE.** 56 cells (21 code, 35 markdown). Structure clean, all 21 cells
  run under warnings-as-errors, Java at `-Xlint:all -Werror`, every number audited. **5 of 23.**
- **Two of my own predictions were refuted by the demos written to confirm them**, and both
  refutations made better sections than the originals. Details in the brief; in short, (a) *any*
  two unequal walker speeds detect a cycle — what actually depends on 1-and-2 is the entry-finding
  phase, and the governing condition is whether (b-a) divides a; (b) scattering a Java LinkedList's
  nodes makes traversal *faster*, because the JVM's compacting collector relays them out in
  reference order, while CPython never moves objects. Rule 8 says fix the demo or rewrite the
  prose; here the honest move was to rewrite the claim and keep the measurement, twice.
- **The branch-count measurement had to change instrument.** `inspect.getsource` cannot see classes
  defined in an exec'd notebook cell, so counting sentinel savings by reading source text failed
  outright. Counting `POP_JUMP_IF*` opcodes with `dis` works under exec, is objective, and is a
  better measurement anyway. It also corrected my number: 7 vs 3 branches, 4 vs 0 structural, not
  the "11 vs 0" I had written from hand-numbered comments.
- **The O(n)-vs-O(n log n) timing wall appeared again** on the delete-with-held-reference demo and
  was resolved the NB-03 way: count the operations. Pointer writes vs element moves is exact
  (n vs ~n²/4), gives a ratio that doubles per size step, and needs no fit at all. This is now the
  standard move and it has not failed yet.
- **The signature difficulty came out more nuanced than the brief predicted.** The brief said the
  cache-miss gap would be order-of-magnitude; in Python it is only ~1.5x against an equivalent
  loop, because CPython's list is itself an array of pointers to boxed ints, so both sides chase
  pointers. The order-of-magnitude claim is true in Java (~30x) and the notebook now measures both
  and explains why they differ, rather than quoting whichever supports the thesis.
- **Stored outputs and hygiene:** 30 outputs via nbclient, no stderr, output scan finds no leaked
  paths, no bare `---` hrules, Quarto renders, structure re-verified.
- **Next:** NB-05 Stacks, Queues & Deques — where §3.3's `ArrayDeque` result gets its own notebook
  and the circular buffer that beat `LinkedList` at queueing is built from scratch.

### 2026-09-08 (NB-03)
- **NB-03 Hashing & Hash Tables: COMPLETE.** 58 cells (23 code, 35 markdown). Structure clean,
  all 23 cells run under warnings-as-errors, Java at `-Xlint:all -Werror`, every number audited
  against printed output. **4 of 23.**
- **The signature difficulty landed as a two-sided story that was not in the brief.** The brief
  said "construct colliding keys, measure O(n) degradation, connect to PYTHONHASHSEED". What the
  measurement actually showed is sharper: Python and Java each defend exactly the axis the other
  leaves open — Python randomises string hashes (so the one-line Java collision family is
  harmless) but leaves int hashes fixed (so `hash(i)==i mod 2^61-1` floods the dict to O(n^2));
  Java can't randomise its published String.hashCode but treeifies buckets (so the same attack is
  ~10x flat, not quadratic). The notebook now has a three-row comparison table as its climax.
- **Two of my own measurement confounds were caught in the audit, both the same species as
  NB-02's join bug.** (1) Two-sum's O(n) timing wandered across the O(n)/O(n log n) boundary
  run-to-run; I switched to counting elements examined (exactly 2.00 per doubling), per NB-00
  §1.7. (2) The "Python shrugs off the Java collision family" cell first reported a spurious ~10x
  because it timed the string *construction*, not the insertion, and the colliding keys are longer
  strings; fixed by building keys in `setup` and comparing against a same-length control. Both are
  the "measure the thing you are claiming about" lesson again — third and fourth instances now.
- **Two bugs are caught by tooling rather than by me, and both became teaching moments.** The
  open-addressing delete-without-tombstone bug is caught by the stress test's *reachability*
  invariant (minimised to three operations); the buggy version keeps its counters consistent, so
  a numeric invariant would have missed it. The `equals`-without-`hashCode` bug is caught by
  `javac -Xlint:all -Werror` outright — you have to `@SuppressWarnings` to even demonstrate the
  runtime damage.
- **A path leak in stored output, caught by the scan and fixed at source.** The deliberate `javac`
  error prints the temp compile directory; the cell now strips it to the bare `BrokenKey.java`
  filename with a regex. Same class as the ML series' AppData leaks — the output scan is now part
  of the per-notebook close, not an afterthought.
- **Stored-outputs backlog stays closed:** NB-03 executed with `nbclient` (50 outputs), stderr
  dropped, no leaked paths, structure re-verified clean. NB-00/01/02 already carry outputs.
- **The NB-00 §3.2 / NOT SEPARABLE story recurred once more** (two-sum), and this time the harness
  verdict plus the count-operations fallback handled it without any prose gymnastics. The pattern
  is now fully routinised: if timing won't separate O(n) from O(n log n), count the operations.
- **Next:** NB-04 Linked Lists — where §1.3's chains and Practice 4's LRU cache both come due, and
  the cache-locality theme from NB-01 §3 returns as the linked list's central weakness.

### 2026-09-08 (NB-02)
- **NB-02 Strings & String Algorithms: COMPLETE.** 39 cells (18 code, 21 markdown). Structure
  clean, all 18 cells run under warnings-as-errors, Java at `-Xlint:all -Werror`, every number
  audited against printed output. **3 of 23.**
- **The `NOT SEPARABLE` verdict predicted in the NB-01 entry is now implemented** in
  `growth_table`, and it fired twice in NB-02 (the Z-algorithm and KMP growth tables) exactly
  where it should. That closes a problem that had recurred in four sections across three
  notebooks: O(n) and O(n log n) are not distinguishable by timing over an 8× range of sizes, and
  the harness now says so instead of forcing a wrong pick. Verified it still rejects a genuinely
  wrong claim.
- **The size cliff in CPython's `+=` was an unplanned finding** and became the best thing in the
  notebook. Detail in the NB-02 brief. It came from refusing to accept a table whose last ratio
  was 5× when the prose said "near-linear" — the ratio was reproducible across trials, so it was
  real, and chasing it turned one cliff into two.
- **I had the join measurement wrong, not the code.** `''.join` fitted O(n log n) and the harness
  rejected my O(n) claim; the cause was that the timed function included the list-building loop.
  Timing the join alone with `setup=` gives err 0.005. The harness catching my own methodology
  error is the second time this has happened (NB-01's `getsizeof`), and both times it was worth
  more than the section it interrupted.
- **`verify_notebook.py` needed a UTF-8 fix.** NB-02 prints a G clef and emoji; on Windows the
  child process encoded stdout as cp1252 and died in its own encoder, which presented as a
  failing cell. The runner now forces `PYTHONIOENCODING=utf-8`/`PYTHONUTF8=1` on the child, and
  the verifier reconfigures its own stdout with `backslashreplace` so that reporting a failure
  can never itself fail. NB-00 and NB-01 re-verified clean afterwards.
- **Prose that cites timings is now written as ranges, not exact figures.** Timing-derived numbers
  move run to run, so exact quotes go stale the moment the notebook is re-executed; deterministic
  numbers (comparison counts, stress counts, Unicode lengths, collision counts) are still quoted
  exactly.
- **Stored-outputs backlog: closed.** NB-00 (46 outputs), NB-01 (44) and NB-02 (39) were executed
  with `nbclient` rather than by hand in VSCode, so this no longer needs a manual Run All. The
  script lives in the scratchpad; it runs each notebook from its own directory, drops every
  `stderr` stream (they carry environment paths) and preserves the file's newline style. All three
  re-verify structure-clean afterwards and the output scan finds no leaked absolute paths.
- **Done next:** NB-03 Hashing & Hash Tables, which picks up §2.4's rolling hash and its adversarial
  worst case as a topic in its own right.

### 2026-09-08 (NB-01)
- **NB-01 Arrays & Dynamic Arrays: COMPLETE.** 43 cells (21 code, 22 markdown). Structure clean,
  all 21 cells run under warnings-as-errors, Java at `-Xlint:all -Werror`, every number audited.
  **2 of 23.**
- **Four demos failed to demonstrate their lesson and were rebuilt** (details in the brief). The
  most useful correction was my own measurement being wrong rather than the code: comparing
  `getsizeof(list)` with `getsizeof(array.array)` reported an 8.5x memory difference as no
  difference at all, because it silently omits the int objects the list points at.
- **The honest finding worth carrying forward:** `array.array` saves 8.5x memory *and* is 2.6x
  slower to sum from Python. The compact representation is not a free win, and the notebook says
  so rather than selling it.
- **NB-00 §3.2 recurred a third time.** Three genuinely-linear cells fitted as O(n log n). The
  claims were dropped in favour of reading the ratio column. If this happens again in NB-02,
  consider making `growth_table` report "O(n) or O(n log n), not separable at these sizes" as a
  first-class verdict rather than picking one.
- **The scratchpad venv did not survive the session boundary**, exactly as §2 warns. Rebuilt with
  matplotlib only — DSA needs nothing else, and `verify_notebook.py`'s runner imports matplotlib
  unconditionally. Note `python -m venv` over a partially-deleted venv directory produced a broken
  pip; creating a fresh directory fixed it.
- **The stored-outputs backlog is closed for everything except NB-01.** All 16 ML notebooks and
  NB-00 now carry outputs. NB-01 needs one Run All + save.
- **Next:** NB-02 Strings & String Algorithms, which picks up §2.4's quadratic accident in its
  most famous form.

### 2026-09-07 (NB-00) — first notebook complete
- **NB-00 Complexity: COMPLETE.** 54 cells (28 code, 26 markdown). Structure clean, all 28 cells
  run under warnings-as-errors, Java compiled with `-Xlint:all -Werror`, every number audited.
  **1 of 23.**
- **The JDK blocker is cleared:** Temurin **21.0.12**, installed via winget, not on PATH, located
  by the toolkit. §10 records the exact path.
- **`dsa_toolkit.py` was verified before anything depended on it**, which is the whole reason the
  plan puts NB-00 first and alone.
- **Three demos failed to demonstrate their lesson and were rebuilt** (details in the brief). The
  most useful was §3.2: my claimed result turned out to be one unstable draw, and measuring the
  instability directly — 8 runs, verdict flipping 5:3 — is a better section than the one I set
  out to write.
- **A bug in my own verification code became §3.1.** Re-seeding an RNG per element yields an
  all-equal list, silently converting insertion sort's average case into its best case.
- **`tools/verify_notebook.py` needed two fixes** to run a notebook that imports a sibling module:
  `cwd`, and `sys.path`. The first alone was not enough. Regression-checked against ML NB-04.
- **Process failure worth recording.** `build_nb00.py` was derived from the NB-13 builder with
  `sed`, and the `OUT =` substitution silently failed to match (forward slashes in the pattern,
  backslashes in the file), so the first build **overwrote
  `ML-Zero-to-Hero/time_series_zero_to_hero.ipynb`**. Recovered exactly with `git checkout`,
  because it had been committed. **Rule: check a derived builder's `OUT` path before running it,
  and do not derive builders by `sed` on a Windows path.**
- **Next:** NB-01 Arrays & Dynamic Arrays, which picks up §1.5's amortised argument and §1.2's
  cache measurements.

### 2026-09-07 — plan created
- Folder `DSA-Zero-to-Hero/` created; this plan written. **No notebooks yet: 0 of 23.**
- Three shaping decisions taken by the owner: **Python + Java side by side**, **finer-grained
  roster**, **foundations first**. All three are the most demanding option available, which is
  recorded here because it explains why the per-notebook budget is 55–70 cells rather than the ML
  series' ~52.
- Roster settled at **23** rather than the requested ~22; §3 gives the three merges that were
  considered and rejected, each because merging would bury a proof.
- **Checked the environment rather than assuming it: there is no JDK on this machine.** `java`,
  `javac`, `jshell`, `mvn` and `gradle` are all absent, `JAVA_HOME` is unset, and no JDK exists in
  any of the standard install locations. `winget` is available, so the fix is one command (§2).
  This blocks the Java half of every notebook and is the first thing to resolve.
- Confirmed reusable from the ML series: `tools/verify_notebook.py` and `tools/check_links.py`
  need no changes. Python on PATH is 3.14.7 with no packages; the venv recipe in §2 still applies.
- Surveyed the two existing tracker notebooks (§4). Between them they cover 24 topics as
  checklists with no implementations, no measured complexity, no Java and no proofs — so they are
  a good topic map and are superseded rather than extended.
- The quality bar (§6) is deliberately **stricter** than the ML series': differential testing
  against a reference, cross-language equivalence testing, measured rather than asserted
  complexity, and invariants asserted in code. All four are cheap in DSA and were impossible in
  ML, and rules 1–5 are what will make this series worth more than the trackers it replaces.
- One process lesson carried over and written into §8 step 9: the ML series finished with nine of
  sixteen notebooks lacking stored outputs, because saving was deferred to the end. Save outputs
  as each notebook lands.
