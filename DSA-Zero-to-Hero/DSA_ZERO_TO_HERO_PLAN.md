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
| 00 | **Complexity, Amortised Analysis & the Measurement Harness** | `complexity_zero_to_hero.ipynb` | ⬜ | — | — |
| 01 | **Arrays & Dynamic Arrays** | `arrays_zero_to_hero.ipynb` | ⬜ | — | — |
| 02 | **Strings & String Algorithms** | `strings_zero_to_hero.ipynb` | ⬜ | — | — |
| 03 | **Hashing & Hash Tables** | `hashing_zero_to_hero.ipynb` | ⬜ | — | — |
| 04 | **Linked Lists** | `linked_lists_zero_to_hero.ipynb` | ⬜ | — | — |
| 05 | **Stacks, Queues & Deques** | `stacks_queues_zero_to_hero.ipynb` | ⬜ | — | — |
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

**0 of 23 done.**

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

### NB-00 — Complexity, Amortised Analysis & the Measurement Harness ⬜
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

### NB-01 — Arrays & Dynamic Arrays ⬜
- **Unique theory:** contiguous memory and O(1) indexing; the growth-factor argument and
  **amortised O(1) append proved three ways**; why 2x (Java `ArrayList`) versus ~1.125x (CPython
  `list`) and what that trades; insert/delete in the middle.
- **Must cover:** prefix sums and difference arrays; two pointers; sliding window — all derived
  as consequences of contiguity rather than presented as tricks.
- **Signature difficulty:** cache locality. Measure array-of-structs vs struct-of-arrays, and
  row-major vs column-major traversal of a 2-D array; the ratio is large and surprising.
- **Java angle:** `int[]` vs `Integer[]` boxing, `ArrayList` internals, `System.arraycopy`.
- **Bad at:** insertion, unknown final size, sparse data.

### NB-02 — Strings & String Algorithms ⬜
- **Unique theory:** immutability and its consequences; the **O(n²) concatenation trap**, measured,
  and why CPython sometimes hides it; string builders; character encodings and why `len()` can
  surprise you.
- **Must cover:** naive matching, **KMP with the prefix function derived**, Z-algorithm,
  Rabin-Karp with rolling hashes and its collision risk.
- **Signature difficulty:** the gap between the O(nm) worst case and the near-linear average that
  makes naive matching survive in practice; construct the adversarial input that breaks it.
- **Java angle:** `String` vs `StringBuilder` vs `StringBuffer`, the interning pool, `char` vs
  code point.
- **Bad at:** Unicode-correct operations, which almost every implementation gets wrong.

### NB-03 — Hashing & Hash Tables ⬜
- **Unique theory:** what a hash function must guarantee; **chaining vs open addressing** with
  both implemented; load factor and the resize policy; why expected O(1) is not worst-case O(1).
- **Must cover:** the frequency-map, duplicate-detection and grouping patterns as applications,
  not as the topic.
- **Signature difficulty:** **the adversarial input.** Construct colliding keys and measure the
  table degrade to O(n); connect to real hash-flooding DoS and to Python's `PYTHONHASHSEED`.
- **Java angle:** `hashCode`/`equals` contract and what breaks when you violate it; `HashMap`'s
  treeification at 8 entries per bucket; why mutable keys are a bug.
- **Bad at:** ordering, range queries, worst-case guarantees, memory overhead.

### NB-04 — Linked Lists ⬜
- **Unique theory:** node-and-pointer layout; singly/doubly/circular; **sentinel nodes** and how
  much special-case code they delete; pointer surgery done carefully.
- **Must cover:** fast/slow pointers with the cycle-detection proof (why Floyd's tortoise and hare
  must meet); reversal iteratively and recursively; merging.
- **Signature difficulty:** **linked lists are usually the wrong answer.** Measure traversal
  against an array of the same length; the cache-miss gap is order-of-magnitude. Then state the
  cases where they genuinely win — O(1) splice with a held reference, LRU caches, intrusive lists.
- **Java angle:** `LinkedList` vs `ArrayList` benchmarked; why the JDK's own docs discourage it.
- **Bad at:** indexing, locality, memory per element.

### NB-05 — Stacks, Queues & Deques ⬜
- **Unique theory:** LIFO/FIFO as invariants; array-backed vs node-backed; the **circular buffer**;
  the **two-stack queue** and its amortised O(1) proved by the accounting method.
- **Must cover:** the **monotonic stack** derived from its invariant, then applied (next greater
  element, largest rectangle in histogram, daily temperatures).
- **Signature difficulty:** monotonic-stack problems are hard because the invariant is implicit;
  the notebook makes it explicit and asserts it inside the loop.
- **Java angle:** why `Stack` is legacy and `ArrayDeque` is the answer; `Queue` vs `Deque`.
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

- [ ] **Install a JDK** (§2). Blocking for everything Java. Record the version here when done.
- [x] **Language** — Python and Java side by side. Decided 2026-09-07 by the owner.
- [x] **Granularity** — finer-grained; 23 notebooks (§3). Decided 2026-09-07.
- [x] **Emphasis** — foundations first (§1). Decided 2026-09-07.
- [ ] **Java-in-notebook mechanism.** Proposed: Python cells that pass Java source to
      `run_java()` from `dsa_toolkit.py`, so one notebook and one kernel per topic and
      `verify_notebook.py` keeps working unchanged. The alternative — an IJava kernel and separate
      Java notebooks — doubles the file count, breaks the side-by-side comparison that motivated
      the bilingual choice, and cannot be verified by the existing gate. **Confirm before NB-00.**
- [ ] **Does the repo root `README.md` get a DSA section now, or when NB-00 lands?** Proposed:
      when NB-00 lands, so the README never advertises an empty folder.
- [ ] **A `PROBLEM_LOG.md`** in this folder, modelled on tracker 2's problem log — worth it once
      three or four notebooks exist and there is something to log.
- [ ] **Practice problems (Part 5): where do they come from?** They must be real and correctly
      titled (rule 10). Proposed: name the problem and its source (LeetCode title, not number —
      numbers change), and never invent one.
- [ ] `tools/verify_notebook.py`'s docstring still references the deleted `ZERO_TO_HERO_PLAN.md`.
      Harmless, but fix it when the file is next touched.

***

## 11. Status log

Append a dated entry every session. Newest first.

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
