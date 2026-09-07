# Zero-to-Hero Notebook Series — Plan & Status

> **If you are a fresh session with no memory of this project: read this file top to
> bottom before touching anything.** It is the single source of truth for what we are
> building, the quality bar, how to build and verify, and what is done so far.
> Update the **Status dashboard** and the **Status log** at the end of every work session.

**Last updated:** 2026-09-06
**Reference implementation:** [`ML-Zero-to-Hero/linear_regression_zero_to_hero.ipynb`](ML-Zero-to-Hero/linear_regression_zero_to_hero.ipynb) — copy its structure and depth.

---

## 1. Status dashboard

Legend: ✅ done · 🚧 in progress · ⬜ not started · ⏸ deferred

| # | Notebook | File | Status | Cells | Verified |
|---|---|---|---|---|---|
| 00 | **ML Foundations (shared)** | `ML-Zero-to-Hero/ml_foundations_zero_to_hero.ipynb` | ✅ | 78 (40 code) | ✅ struct + run |
| 01 | **Linear Regression** | `ML-Zero-to-Hero/linear_regression_zero_to_hero.ipynb` | ✅ | 157 (77 code) | ✅ struct + run |
| 02 | **Logistic Regression** | `ML-Zero-to-Hero/logistic_regression_zero_to_hero.ipynb` | ✅ | 62 (35 code) | ✅ struct + run |
| 03 | **Decision Trees** | `ML-Zero-to-Hero/decision_trees_zero_to_hero.ipynb` | ✅ | 51 (28 code) | ✅ struct + run |
| 04 | **Random Forest & Bagging** | `ML-Zero-to-Hero/random_forest_zero_to_hero.ipynb` | ✅ | 44 (26 code) | ✅ struct + run |
| 05 | **Gradient Boosting (+ XGB/LGBM/CatBoost)** | `ML-Zero-to-Hero/gradient_boosting_zero_to_hero.ipynb` | ✅ | 46 (25 code) | ✅ struct + run |
| 06 | **Support Vector Machines** | `ML-Zero-to-Hero/svm_zero_to_hero.ipynb` | ✅ | 50 (28 code) | ✅ struct + run |
| 07 | **K-Nearest Neighbors** | `ML-Zero-to-Hero/knn_zero_to_hero.ipynb` | ✅ | 52 (24 code) | ✅ struct + run |
| 08 | **Naive Bayes** | `ML-Zero-to-Hero/naive_bayes_zero_to_hero.ipynb` | ✅ | 61 (30 code) | ✅ struct + run |
| 09 | **PCA & Dimensionality Reduction** | `ML-Zero-to-Hero/pca_zero_to_hero.ipynb` | ✅ | 57 (28 code) | ✅ struct + run |
| 10 | **K-Means & Clustering** | `ML-Zero-to-Hero/kmeans_zero_to_hero.ipynb` | ✅ | 56 (29 code) | ✅ struct + run |
| 11 | **Imbalanced Classification** | `ML-Zero-to-Hero/imbalanced_classification_zero_to_hero.ipynb` | ✅ | 46 (22 code) | ✅ struct + run |
| 12 | Explainable AI | `ML-Zero-to-Hero/explainable_ai_zero_to_hero.ipynb` | ⬜ | — | — |
| 13 | Time Series Forecasting | `ML-Zero-to-Hero/time_series_zero_to_hero.ipynb` | ⬜ | — | — |
| 14 | Recommender Systems | `ML-Zero-to-Hero/recommender_systems_zero_to_hero.ipynb` | ⬜ | — | — |
| 15 | Anomaly Detection | `ML-Zero-to-Hero/anomaly_detection_zero_to_hero.ipynb` | ⬜ | — | — |

**Total planned: 16 notebooks** (1 shared foundations + 15 topic notebooks). **12 of 16 done.**

**Scale, measured rather than projected.** The original estimate of ~150 cells each (≈ 2,300
total) was made before NB-00 existed. Extracting the shared workflow into NB-00 cut topic
notebooks to roughly a third of that:

| | Cells |
|---|---|
| NB-01 (written before NB-00 existed) | 157 |
| NB-00 (the shared foundations) | 78 |
| NB-02..11 (the post-NB-00 template) | 44–62, **~52 average** |
| **Built so far (12 notebooks)** | **760** |
| Projected total for 16 | **~968** |

So by cell count the series is **~79% built** (760 of ~968) while being 12 of 16 by notebook
count. The gap is NB-01: it alone is 16% of the projected total, and every remaining notebook
is template-sized. The remaining four are NB-12 (Explainable AI) and the three applied problem
types (13–15), which have less prior art in the repo to draw on than the algorithm notebooks
did.

Treat each as its own project with its own verification pass.

### Where the files live

```
Self-Prep/
├── ZERO_TO_HERO_PLAN.md            <- this file: plan, quality bar, status log
├── ML-Zero-to-Hero/                <- all series notebooks live here
│   ├── README.md                   <- the reader-facing guide and reading order
│   ├── ml_foundations_zero_to_hero.ipynb
│   ├── linear_regression_zero_to_hero.ipynb
│   ├── logistic_regression_zero_to_hero.ipynb
│   ├── decision_trees_zero_to_hero.ipynb
│   ├── random_forest_zero_to_hero.ipynb
│   ├── gradient_boosting_zero_to_hero.ipynb
│   ├── svm_zero_to_hero.ipynb
│   ├── knn_zero_to_hero.ipynb
│   ├── naive_bayes_zero_to_hero.ipynb
│   ├── pca_zero_to_hero.ipynb
│   ├── kmeans_zero_to_hero.ipynb
│   └── imbalanced_classification_zero_to_hero.ipynb
└── tools/
    ├── verify_notebook.py          <- the quality gate
    └── check_links.py              <- relative-link checker (see 7)
```

Twelve of the sixteen exist. Add each new file to this tree when it lands.

**Two READMEs, two audiences — keep them distinct:**

- `ML-Zero-to-Hero/README.md` is for **the reader/student**: reading order, suggested paths,
  how to run them. Update its status table and progress count when a notebook lands.
- `ZERO_TO_HERO_PLAN.md` (this file) is for **whoever is building them**: quality bar, build
  and verify workflow, per-notebook briefs, and the status log of what broke and why.

**Relative-link rule after the move:** notebooks link to each other by bare filename (same
folder) and to this plan as `../ZERO_TO_HERO_PLAN.md`. Anything outside the folder — the
trackers, `tools/` — needs a `../` prefix. Run the link check in §7 after adding a notebook.

### Reading order (what the folder README tells students)

Grouped by dependency, not by syllabus convention:

| Group | Notebooks | Why this grouping |
|---|---|---|
| **Foundations — read first** | 00 | Every other notebook assumes it and does not repeat it |
| **The core four** | 01, 02, 03, 04 | The models everything later is measured against; 03 → 04 is a deliberate cliffhanger (instability → averaging) |
| **Remaining algorithms** | 05–10 | Each stands alone once the core four are done |
| **Cross-cutting** | 11, 12 | Reference the models above, so they land better afterwards |
| **Applied problem types** | 13, 14, 15 | Whole problem shapes rather than single algorithms |

Build order and reading order are **the same**, deliberately — so a partially finished series
is still a coherent course rather than a set of gaps.

---

## 2. What this project is

Turn each section of [`ml_study_tracker_2_classical_ml.ipynb`](ml_study_tracker_2_classical_ml.ipynb)
(a terse checklist tracker: 12–16 cells, 5–7 checklist items per topic) into a **standalone,
runnable, zero-knowledge-to-job-ready notebook**. Target length is **~50 cells** since NB-00
absorbed the shared workflow — the ~150-cell figure in the original plan applies only to NB-01,
which was written before that split.

**The audience:** someone who has never fitted a model, who needs to end up able to build,
diagnose, tune and *defend* the model in an interview or a code review.

**The bar:** every claim in prose matches what the code actually prints; every code cell runs
clean; the reader is told what the method cannot do, not just what it can.

---

## 3. Scope decisions already made

| Decision | Rationale |
|---|---|
| **16 notebooks, not 20** | The tracker has 16 sections. Unsupervised extras (Hierarchical, DBSCAN, GMM, t-SNE) are folded into NB-10 rather than getting their own files. |
| **Merge Gradient Boosting with XGBoost/LightGBM/CatBoost** (NB-05) | They share all their theory. Splitting means deriving boosting twice, and the libraries notebook would have no theory of its own. |
| **Add a shared Foundations notebook (NB-00)** | ~49 of the LR notebook's 157 cells are algorithm-agnostic (workflow, syntax, messy data, error appendix). Writing those 15 more times means fixing every future bug in 16 places. NB-00 holds them once; topic notebooks link to it and spend their cells on what is unique. |
| **Build order = payoff order, not tracker order** | NB-02..05 (LogReg, Trees, RF, Boosting) are what interviews and real tabular work actually hit. Cross-cutting topics (11–12) land better once the algorithms exist to reference. |
| **The `.ipynb` is the source of truth** | Notebooks are built from generator scripts in a session scratchpad. That scratchpad is **gone** after a context reset. Do not rely on it — edit notebooks directly, or write a fresh generator into `tools/` if you want one. |
| **Notebooks live in `ML-Zero-to-Hero/`** | Moved 2026-09-06. Keeps the series together and separates it from the older tracker notebooks at the repo root. Links inside notebooks use bare filenames for siblings and `../` for anything outside. |

---

## 4. Repo context — what already exists

Do **not** duplicate these; mine them for material and link to them.

| File | Covers | Overlap |
|---|---|---|
| `ml_study_tracker_2_classical_ml.ipynb` | The 16 source sections | **This is the input.** Each topic notebook expands one section. |
| `Supervised_Learning_Practical_v4.ipynb` | 10 worked sections: LinReg, LogReg, KNN, DT, RF, GB, SVM+PCA, NB, TimeSeries, CV | Heavy. Its worked examples are a good starting point for Part 4 of NB-02..08, 13. Recently cleaned (see log). |
| `Unsupervised_Learning_Practical_v4.ipynb` | K-Means, Hierarchical, DBSCAN, GMM, PCA, t-SNE, Isolation Forest | Feeds NB-09, NB-10, NB-15. |
| `ml_study_tracker_1_foundations_workflow.ipynb` | NumPy/Pandas, EDA, splitting, CV, pipelines | Feeds **NB-00**. |
| `Deep_Learning_Practical_v2.ipynb`, `ml_study_tracker_3_*` | Deep learning / GenAI / MLOps | Out of scope for this series. |

---

## 5. The canonical template

NB-01's structure, with actual cell counts. Keep the part numbering identical across all
notebooks so a reader can jump between them.

| Part | Content | Cells (NB-01) | Reusable? |
|---|---|---|---|
| — | Title, one-paragraph summary, contents table, suggested reading paths | 1 | shape only |
| **0** | Setup: conditional install cell + one master import cell | 3 | ✅ near-identical |
| **1** | **Theory from zero** — build the model up in ~10 numbered steps; implement from scratch and check against sklearn in the same cell | 42 | ❌ unique |
| **2** | **End-to-end flow** — ASCII pipeline diagram, leakage demo, `Pipeline`, cross-validation | 10 | ✅ → NB-00 |
| **3** | **Syntax cheat sheet** — the sklearn API, constructors, preprocessing, metrics, persistence | 18 | ✅ mostly → NB-00 |
| **4** | **Worked example** — one real dataset, all 10 flow steps, nothing skipped | 28 | ❌ unique |
| **5** | **Real-world data problems** — missing values, outliers, mixed types, feature engineering, target transforms | 17 | ✅ → NB-00 |
| **6** | **Uncertainty & inference** — prediction intervals, conformal, p-values, extrapolation, when to stop | 14 | ~half unique |
| **7** | **Tough questions** — 12 questions with `<details>` answers + 3 coding challenges | 7 | ❌ unique |
| **8** | **Practice datasets** — 5 datasets, ordered by difficulty, each with a brief | 10 | shape only |
| **9** | **Reading the literature** — how to read a paper + the papers behind each section | 6 | ❌ unique |
| — | Appendix: common errors, sanity checklist, where to go next | 1 | ✅ → NB-00 |

**After NB-00 exists**, topic notebooks drop Parts 2, 3, 5 and the Appendix down to a short
"see Foundations" pointer. The original guess was ~100 cells; **measured across NB-02..08 the
real figure is 44–62, averaging ~52.** Do not pad a notebook to hit a cell count — NB-04 is
the shortest at 44 and is not the weakest.

### The part numbering topic notebooks actually use

The table above is **NB-01's** layout, kept because it explains what NB-00 absorbed. Every
notebook from NB-02 onward uses this shorter numbering instead, and new notebooks should match
it exactly:

| Part | Content |
|---|---|
| — | Title, why-this-matters, contents table, one-paragraph summary |
| **0** | Setup: conditional install cell + one master import cell |
| **1** | **Theory from zero** — numbered steps, from scratch, checked against sklearn |
| **2** | **Worked example** — one dataset, end to end |
| **3** | **The topic's signature problem**, in depth |
| **4** | **Tough questions** — ~12 with `<details>` answers + 3 coding challenges |
| **5** | **Practice datasets** — 5, ordered by difficulty, each with a brief |
| **6** | **Reading the literature** — the papers behind each section |
| — | Appendix: topic-specific errors table, ship checklist, where to go next |

### Conventions that make them feel like one series

(Part numbers below are the topic-notebook ones — 4, 5, 6 — not NB-01's 7, 8, 9.)

- Part 5 dataset briefs always carry: **what it is / why this one / your brief (numbered) /
  a good result / the trap**.
- Part 4 answers hide in `<details><summary>Answer</summary> ... </details>`.
- Part 6 always has: 2–3 "start here" papers with a note on why → a "paper behind each
  section" table with ✅ free / 🔍 search-the-title markers → an "if you read only one"
  recommendation.
- Prose voice: plain, direct, willing to say a model is mediocre. No hype.
- Every table that reports a model's score also reports a **baseline** (`DummyRegressor` /
  `DummyClassifier`) on the same line or immediately above.

---

## 6. Quality bar — non-negotiables

These were all learned the hard way while building NB-01. Violating them produces a notebook
that looks fine and teaches something false.

1. **Every code cell must run, in order, with `warnings.simplefilter("error")`.**
   A warning is a failure. Run `tools/verify_notebook.py <nb> --run` before declaring done.
2. **Verify every numeric claim in prose against the actual printed output.** Do not write
   "the log transform is the big win" and then discover it gave 0.2%. Run the cell, read the
   number, *then* write the sentence. This caught 6 wrong claims in NB-01.
3. **A demo must actually demonstrate its lesson.** NB-01's first overfitting demo was
   numerically pathological (degree-15 polynomials made the design matrix rank-deficient, so
   lstsq silently self-regularised and the "too much alpha underfits" claim was false).
   Tune the demo until the intended effect is real, then re-verify.
4. **Baselines are mandatory.** No metric is interpretable alone.
5. **Never fabricate a URL, a DOI, or a dataset id.** Fetch it and check. Pin every
   `fetch_openml` call to a `version=` or `data_id=` — unpinned names warn *and* are
   irreproducible.
6. **No stored stderr, no absolute local paths in outputs.** `verify_notebook.py` checks this.
7. **No edit-history archaeology.** Never write "the v2 bug, fixed here" or "in v3 we…". The
   reader has one file. State the lesson, not the changelog.
8. **Finish the features you start.** If the intro promises a question block in every section,
   every section gets one.
9. **Say what the method cannot do.** NB-01's worked example lands at R²=0.45 and says so
   plainly, including "nowhere near good enough for an individual clinical decision".
10. **Notebooks ship WITH outputs** (decided after NB-00/NB-01 — see §10), so a reader
    browsing on GitHub sees the results that back the prose. Whichever state a notebook is in,
    it must be internally consistent: a cell with outputs must carry an `execution_count`.
    `verify_notebook.py` enforces the consistency, not the choice.

### ⚠️ The VSCode hazard

If the target `.ipynb` is **open in VSCode**, an editor save will silently overwrite anything
written to disk from a script, reverting it. This has happened in this repo.

- After writing a notebook, **re-read it from disk** to confirm the change survived.
- Tell the user to reload/close the file in VSCode before continuing.
- `Read` refuses notebooks >256KB, so `NotebookEdit` is unusable on most files here — write
  with a script and verify by re-reading.

---

## 7. Build & verify workflow

### Environment facts

- Notebook kernel is a conda env named **`base`** that is **not on PATH** from the shell.
- `C:\Python314\python.exe` is on PATH but has **no scientific packages**.
- Therefore: create a throwaway venv to verify notebooks. It will not exist in a new session.

```bash
# one-time per session, somewhere outside the repo (e.g. the session scratchpad)
python -m venv <scratch>/venv
<scratch>/venv/Scripts/python.exe -m pip install -q numpy pandas matplotlib scipy scikit-learn
# add per-notebook extras as needed: xgboost lightgbm statsmodels shap
```

Versions every verification has run against: numpy 2.5.2, pandas 3.0.5, scikit-learn 1.9.0.
Note `ndarray.ptp()` was **removed** in NumPy 2 — use `np.ptp(arr)`.

**Datasets that download.** Most notebooks use bundled sklearn data, but NB-08 fetches
20 Newsgroups (~14 MB) and several Part 5 briefs use `fetch_openml`. These cache under
`~/scikit_learn_data`, so the first run of such a cell is slow and later runs are not. A fresh
machine will need network access for the first verification pass.

**Library gotchas already paid for** (do not rediscover these):

| Gotcha | Where |
|---|---|
| `ndarray.ptp()` removed in NumPy 2 | NB-01 |
| `make_column_selector(dtype_include=object)` raises `Pandas4Warning` | NB-00 |
| `OneHotEncoder` sparse output breaks `transform_output="pandas"` | NB-00 |
| `load_digits` emits a NumPy 2.5 `DeprecationWarning` from inside sklearn | NB-02, NB-07 |
| `SVC(probability=True)` deprecated, removal in 1.11 | NB-06 |
| `Nystroem`/`RBFSampler` default `gamma=1.0`, not `"scale"` | NB-06 |
| `k > n_samples_fit` raises rather than degrading | NB-07 |
| `MultinomialNB(alpha=0)` needs `force_alpha=True` **and** still warns | NB-08 |
| `fetch_20newsgroups` **sorts** `categories` — index `target_names` | NB-08 |
| Millisecond fit-time ratios are not reproducible; compute them at runtime | NB-06, NB-08 |
| `np.corrcoef` divides by zero on constant columns | NB-09 |
| sklearn's built-in `"f1"`/`"precision"` scorers warn when nothing is predicted positive | NB-11 |
| pandas 3 `.astype(str)` **decodes** bytes rather than repr-ing them | NB-11 |
| `average_precision_score` does not accept `zero_division` (careless regex hazard) | NB-11 |

### Verify

```bash
python tools/verify_notebook.py ML-Zero-to-Hero/<nb>.ipynb            # structure only
python tools/verify_notebook.py ML-Zero-to-Hero/<nb>.ipynb --run --python <scratch>/venv/Scripts/python.exe

# check every relative link still resolves after adding or moving a notebook
python tools/check_links.py          # exits non-zero if any are broken

# check which notebooks still ship without stored outputs (see 10)
python -c "import io,json,glob,os; [print('%-50s %2d/%2d' % (os.path.basename(p), sum(1 for c in json.load(io.open(p,encoding='utf-8'))['cells'] if c['cell_type']=='code' and c.get('outputs')), sum(1 for c in json.load(io.open(p,encoding='utf-8'))['cells'] if c['cell_type']=='code'))) for p in sorted(glob.glob('ML-Zero-to-Hero/*.ipynb'))]"
```

⚠️ The link checker used to be inlined here as a bash heredoc. It contained a regex full of
backslashes — exactly what the gotcha below mangles — so it is a **script** now. Do not paste
it back inline.

Structure pass checks: cell ids, duplicate ids, syntax, stderr in outputs, local-path leaks,
outputs/execution_count consistency, and edit-history references.
`--run` executes every code cell in order with warnings-as-errors.

### Bash gotcha in this environment

Heredocs mangle backslashes (`\\n` → a real newline), which silently corrupts regexes and
string literals. **Write Python helper scripts with the `Write` tool**, not via `<<'PY'`
heredocs, whenever backslashes are involved. Use `chr(92)` / `chr(10)` if you must inline.

---

## 8. Per-notebook briefs

Build in this order. Each brief gives what is *unique* to that notebook; Parts 0/2/3/5/8/9
follow the template.

> Datasets marked ✅ are verified to load; **candidates** must be fetched and checked first.

---

### NB-00 — ML Foundations (shared) ✅ COMPLETE
78 cells (40 code). Verified: structure clean, all 40 cells run under warnings-as-errors.

**Structure as built** (topic notebooks should reference these part numbers):

| Part | Content |
|---|---|
| 0 | Setup |
| 1 | The workflow (10-step diagram, framing, `DummyRegressor`/`DummyClassifier` baselines) |
| 2 | Splitting & validation (train/test, CV, `KFold`/`Stratified`/`Group`/`TimeSeries` compared on 12 eyeball-able rows, `scoring` sign convention) |
| 3 | **Leakage** — all five types, each demonstrated with the size of the damage |
| 4 | Pipelines & `ColumnTransformer` (+ `make_column_selector`, `set_config(transform_output="pandas")`) |
| 5 | Messy data (missing values, outliers, scalers vs outliers, categorical encoding + dummy trap) |
| 6 | Feature engineering (log/ratio/interaction measured by CV, cyclical encoding, target transforms) |
| 7 | Metrics — regression **and** classification, confusion matrix, ROC vs PR, thresholds, cost-based thresholding, calibration |
| 8 | Tuning (grid vs randomized vs halving, timed; nested CV) |
| 9 | Shipping (persist the pipeline + metadata, extrapolation guard, monitoring table) |
| 10 | Syntax cheat sheet |
| — | Appendix: common errors, pre-ship checklist, where to go next |

**Headline demonstrations** (numbers from the verified run, useful when writing topic notebooks):

- Target leakage: CV ROC-AUC 0.695 → **0.945** by adding one post-outcome column.
- Group leakage: random 5-fold AUC **0.902** vs `GroupShuffleSplit` **0.448** — labels were
  coin flips per patient, so the honest score is chance and *all* apparent skill was
  patient recognition.
- Time leakage: shuffled KFold R² **0.930** vs `TimeSeriesSplit` **0.511**.
- Imbalanced baseline: `DummyClassifier` scores **94% accuracy** with recall 0.
- Randomized search matched an exhaustive grid's optimum in ~26% of the time.

**Note:** NB-01 keeps its own copies of this material — it stays self-contained. Do **not**
retro-strip it. Topic notebooks from NB-02 onward should instead open with a "read NB-00
first" pointer and drop their Parts 2/3/5, landing near ~100 cells.

---

### NB-02 — Logistic Regression ✅ COMPLETE
62 cells (35 code). Verified: structure clean, all 35 cells run under warnings-as-errors,
every printed number checked against its prose.

**Structure as built** — first notebook to use the post-NB-00 shape (Parts 2/3/5 dropped,
replaced by a prerequisite pointer):

| Part | Content |
|---|---|
| 0 | Setup |
| 1 | Theory: why not linear regression · sigmoid & log-odds · **why squared error is wrong** · fitting from scratch (GD) · odds ratios · regularization and `C` · multiclass |
| 2 | Worked example: churn, 7% base rate, mixed types, known planted coefficients |
| 3 | Thresholds & calibration in depth — cost-optimal thresholds, `class_weight` damage, recalibration |
| 4 | 12 tough questions + 3 coding challenges (IRLS from scratch, XOR, proving `class_weight` ≈ intercept shift) |
| 5 | 5 practice datasets |
| 6 | Reading the literature |
| — | Appendix: logistic-specific errors + checklist |

**Headline demonstrations** (verified numbers, reusable when writing later notebooks):

- **Squared error is provably non-convex here** — negative Hessian eigenvalues at
  θ=[4,2], [6,−3], [−5,4]; log-loss is PSD everywhere.
- **Gradient vanishing:** at z=−10 with y=1, squared error's gradient is 9.1e-5 vs
  log-loss's 1.0 — a **11,014×** difference.
- From-scratch GD matches sklearn (`C=1e6`) to 5e-4; **Newton/IRLS needs ~5 iterations
  vs 5,000** for plain GD.
- At threshold 0.5 the model flags **zero** customers — accuracy exactly equals the
  do-nothing baseline — while AUC is 0.754. The cleanest "threshold ≠ model" demo available.
- **`class_weight='balanced'`:** AUC 0.7540 → 0.7535 (unchanged), recall 0.00 → 0.73,
  mean predicted p **5.8× the true rate**, Brier 0.063 → 0.208. Challenge 3 then proves it
  is essentially an intercept shift: Spearman ρ = 0.9999, and re-thresholding the plain
  model reproduces the same recall *and* precision with calibration intact.
- **Gradient boosting LOSES** to logistic regression 0.654 vs 0.749, because the data is
  genuinely linear in log-odds — a useful counterexample to "the fancier model wins".

**Notes for future notebooks:**
- `load_digits` emits a NumPy 2.5 `DeprecationWarning` from inside sklearn 1.9. Use
  `load_wine` for multiclass demos, or suppress deliberately (NB-02 Part 5 does the latter,
  with a comment).
- sklearn's `OneVsRestClassifier.predict_proba` **renormalises**, so "OvR probabilities
  don't sum to 1" must be shown on the raw per-estimator outputs.
- Verified extra datasets: `adult` v2 (48842×14, 8 cat, 6465 NaN), `credit-g` v1 (1000×20),
  `bank-marketing` v1 (45211×16).

---

### NB-03 — Decision Trees ✅ COMPLETE
51 cells (28 code). Verified: structure clean, all 28 cells run under warnings-as-errors,
every printed number audited against its prose.

**Structure as built:** Part 1 theory (recursive partitioning · impurity · **from scratch** ·
greedy ≠ optimal · pruning · scale invariance · regression trees) → Part 2 breast cancer
worked example → **Part 3 instability** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **From-scratch CART gives predictions IDENTICAL to sklearn** (~20 lines, brute-force split
  search + recursion). Same for the regression variant in Challenge 1.
- **Gini vs entropy is not worth tuning:** 0.9300 ± 0.0242 vs 0.9306 ± 0.0257 over 30 folds,
  and they pick the **same root feature in 88/100** bootstrap resamples.
- **Greedy fails on XOR:** every possible first split has gain ≈ 0.001; depth 1 scores 0.527
  (chance), depth 2 scores 1.0000.
- **Scale invariance is exact:** predictions bit-identical after `x*1000+7` **and** after
  `log1p(x)`; logistic regression's are not.
- **Axis-aligned cost:** on a diagonal boundary, logistic regression 0.9967 vs a 44-leaf tree
  0.9783.
- **Regression trees cannot extrapolate:** truth at x=25 is 53, the tree says 23.32 forever
  (training y maxed at 24.34).
- **Instability (the centrepiece):** 60 bootstraps → **5 different root features**, top two
  tied at 20/60 each, while accuracy stays 0.9296 ± 0.0147. Then averaging fixes it:
  one tree 0.9232 ± 0.023 → 100-tree forest 0.9884 ± 0.009. This *derives* the motivation
  for NB-04 rather than asserting it.
- **MDI cardinality bias, isolated** (Challenge 2): with a target depending only on
  `real_signal`, MDI gives 0.268 to pure-noise continuous and 0.249 to a pure-noise unique ID,
  but only 0.019 to pure-noise *binary* — while permutation importance gives all three ~0.

**Notes for later notebooks:**
- Mixing a DataFrame `.fit()` with a numpy `.predict()` (or vice versa) raises a feature-name
  `UserWarning` that fails the verifier. Keep one or the other throughout a cell.
- Verified extra datasets: `titanic` v1 (1309×13, 3855 NaN — has the `boat`/`body` leak),
  `car` v3 (1728×6, all ordinal), plus `Bike_Sharing_Demand` v2 and `adult` v2.

---

### NB-04 — Random Forest & Bagging ✅ COMPLETE
44 cells (26 code). Verified: structure clean, all 26 cells run under warnings-as-errors,
every printed number audited.

**Structure as built:** Part 1 theory (bootstrap · variance formula · **decorrelation** · OOB ·
why more trees never overfit · hyperparameters) → Part 2 credit-risk worked example →
**Part 3 feature importance done properly** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **Bootstrap** converges to 1−1/e: 0.6557 → 0.6322 as n goes 10 → 10,000.
- **The variance formula** $\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$ verified empirically, then
  used to show that at B=500, ρ=0.9 keeps **90%** of the variance and ρ=0.2 keeps 20%.
- **Bagging depends on instability, not bias** (Breiman 1996): deep tree 0.825 → 0.945,
  stump 0.797 → 0.878, **logistic regression 0.8936 → 0.8934 (nothing)**.
- **The decorrelation trade-off, measured:** `max_features` None → sqrt → 1 gives tree
  correlation 0.4287 → 0.3416 → 0.1842 while CV AUC goes 0.9246 → **0.9371** → 0.9211. Both
  extremes lose; that is the whole design of a forest in one table.
- **OOB is mildly pessimistic** and the gap closes with more trees: +0.0243 at 10 trees →
  +0.0067 at 1000.
- **More trees never overfit** vs boosting: forest 0.633 → 0.808 monotone; gradient boosting
  peaks at 0.786 (200 trees) and falls to 0.761 at 800.
- **Prune the base trees and the forest gets worse:** depth 2/4/8/None → 0.833/0.895/0.935/**0.941**.
  Inverts NB-03's advice, and explains why.
- **Correlated-feature importance (the centrepiece):** three near-copies of one driver.
  Single-tree MDI 0.657/0.125/0.036 (arbitrary) → forest MDI 0.237/0.238/0.246 (evened out) →
  permutation all small → **drop one costs ≤0.0065 AUC, drop all three costs 0.2942**.
- **OOB breaks on grouped data** (Challenge 2): OOB 0.9695 vs GroupShuffleSplit 0.6108,
  **+0.359 optimism**, and unlike CV there is no `groups=` argument to fix it.

**Notes for later notebooks:**
- `oob_score=True` with <50 trees emits a `UserWarning`; NB-04 captures it and prints it as a
  table column rather than suppressing (same pattern used in the tracker cleanup).
- Drop-column importance for a *single* feature is noisy — in NB-04's run pure `noise` scored
  a larger loss (0.0071) than a real signal (0.0065). Always repeat across seeds, or group.

---

### NB-05 — Gradient Boosting (+ XGBoost / LightGBM / CatBoost) ✅ COMPLETE
46 cells (25 code). Verified: structure clean, all 25 cells run under warnings-as-errors,
every printed number audited.

**Structure as built:** Part 1 theory (residual fitting · **function-space gradient descent** ·
learning rate ↔ rounds · shallow trees · early stopping · label noise) → Part 2 the libraries →
Part 3 worked example with honest tuning → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **The additive structure proved exactly**: reconstructing sklearn's own prediction as
  `F0 + lr * sum(tree outputs)` matches `.predict()` to **8.9e-15**, and matches
  `staged_predict` at all 50 stages.
- **"Fit the residual" = "fit the negative gradient"**, checked against a finite-difference
  gradient for *both* squared error and log-loss.
- **learning_rate sets the floor:** lr=0.5 bottoms out at RMSE 0.9440 and stays there from 200
  to 1000 trees; lr=0.1 reaches 0.7111.
- **Base-learner depth runs OPPOSITE to NB-04:** boosting 0.986/0.691/0.711/1.297/1.760 for
  depth 1/2/3/6/None, while the forest improves monotonically 2.730 → 1.354. The single best
  cross-notebook contrast in the series.
- **Early stopping:** best test log-loss at round **42**; running to 600 is **+69% worse**.
  Automatic early stopping used 49 rounds and cut log-loss from 0.762 to 0.463 — while AUC
  barely moved, which is the calibration-vs-ranking distinction made concrete.
- **Label noise:** forest wins at every level and the gap widens (−0.005 at flip_y=0 to
  −0.038 at 0.40).
- **Histogram binning:** sklearn exact 25.5s vs LightGBM 0.18s (**139×**) at equal AUC.
- **Challenge 2 — `max_depth` is interaction order:** on a pure x1·x2 target, depth-1 stumps
  sit at chance (0.496) with **1000 rounds**; depth 2 gets 0.991.

**The notable honest result:** in Part 3, 25-configuration `RandomizedSearchCV` improved CV AUC
by +0.0050 — **smaller than the CV std of 0.0077** — and on the test set the tuned model came
out **0.0010 worse** than the defaults. Rather than reroll, the section was rewritten to make
this the lesson, and it now demonstrates Q12 live.

**Notes for later notebooks:**
- xgboost 3.4.1 / lightgbm 4.7.0 / catboost 1.2.10 all install and work; Part 0 detects them
  and the library sections degrade gracefully if any are missing.
- CatBoost native categorical (0.8369) > one-hot (0.8334) > LightGBM native (0.8208) on a
  60-level column — native handling is *not* automatically better.
- **Unique theory:** boosting as gradient descent *in function space*; fitting the negative
  gradient (= residual for squared error); shrinkage/learning-rate ↔ n_estimators trade-off;
  why base learners are deliberately shallow; early stopping.
- **Library section:** the three libraries' real differences — histogram binning (LGBM),
  leaf-wise vs level-wise growth, `scale_pos_weight`, native categorical handling (CatBoost's
  ordered target statistics), missing-value routing. Include `HistGradientBoostingRegressor`
  as the no-extra-dependency option.
- **Must cover:** honest stage selection on validation (not test); boosting's sensitivity to
  mislabelled rows; a head-to-head vs Random Forest with identical sample weights.
- **Traps:** tuning `n_estimators` without tuning `learning_rate`; comparing libraries with
  mismatched weighting.
- **Papers:** Friedman (2001) *Greedy Function Approximation*; Friedman (2002) *Stochastic
  Gradient Boosting*; Chen & Guestrin XGBoost (2016); Ke et al. LightGBM (2017);
  Prokhorenkova et al. CatBoost (2018). All free — verify links.
- **Extra deps:** `xgboost`, `lightgbm`, optionally `catboost`.

---

### NB-06 — Support Vector Machines ✅ COMPLETE
50 cells (28 code). Verified: structure clean, all 28 cells run under warnings-as-errors,
every printed number audited.

**Structure as built:** Part 1 theory (max margin · support vectors · soft margin & `C` ·
hinge loss · **the kernel trick** · RBF & `gamma` · scaling) → Part 2 digits worked example →
**Part 3 the practical limits** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **Kernel trick verified exactly:** explicit 6-D φ(x)·φ(z) equals (1+x·z)² to **4.4e-16**;
  the map's dimension is printed growing 6 → 5,151 → 501,501 for d = 2 → 100 → 1000.
- **Only support vectors matter:** refitting on the 13% that were SVs gives w identical to
  **2.9e-11** and **byte-identical predictions** on all 300 points.
- **Circles:** linear 0.5125 (chance), poly 0.6542, RBF **1.0000** — and a hand-built
  r = x₁²+x₂² feature with a *linear* SVM also gets 1.0000, showing what the kernel does.
- **Scaling is the biggest single lever:** 0.9064 → **0.9766** from adding a `StandardScaler`,
  while a random forest on the same raw features is untroubled.
- **C×gamma is a genuine 2-D ridge:** best at C=1, γ=0.1 (0.8762); the whole C=0.01 row is at
  chance and the γ=1.0 column collapses.
- **Scaling wall:** SVC fit time ~ **n^1.73** (LinearSVC ~n^1.00); 3.0s at 16k rows
  extrapolates to ~20 minutes at 500k for a *single* fit.
- **Challenge 2:** flipping a FAR point barely rotates the SVM boundary; flipping a NEAR one
  rotates it much more — while logistic regression responds to both.

**Two findings worth carrying forward:**

1. **`SVC(probability=True)` is DEPRECATED in sklearn 1.9**, removal in 1.11. Replacement is
   `CalibratedClassifierCV(SVC(), ensemble=False)`. Same ~6× cost, but internally consistent
   (its `predict` and `predict_proba` agree exactly, which the old API did not). §3.2 and Q9
   are written around the new API.
2. **`Nystroem` / `RBFSampler` do NOT inherit SVC's `gamma="scale"` default** — they default to
   `gamma=1.0`. Left at the default, RBFSampler+SGD scored **0.5150** (chance); with
   `gamma=1/(p·var)=0.05` it scored **0.9167**. Kept in the notebook as a labelled failure row
   because nothing warns you.

**(original brief follows)**

- **Unique theory:** maximum-margin intuition; hard vs soft margin; hinge loss; the dual and
  why only support vectors matter; **the kernel trick** derived properly (never form φ(x));
  RBF/poly kernels; `C` and `gamma` as a 2-D bias-variance grid.
- **Worked example:** `load_digits` ✅ with PCA (as in `Supervised_Learning_Practical_v4` §7).
- **Must cover:** scaling is mandatory; SVC does not give probabilities without
  `probability=True` (and that refits with Platt scaling — expensive and sometimes worse);
  O(n²–n³) scaling → `LinearSVC`/`SGDClassifier` for big data.
- **Papers:** Cortes & Vapnik (1995); Boser, Guyon & Vapnik (1992).

---

### NB-07 — K-Nearest Neighbors ✅ COMPLETE
52 cells (24 code). Verified: structure clean, all 24 cells run under warnings-as-errors,
every printed number audited.

**Structure as built:** Part 1 theory (lazy learning · the scaling trap · k as a
bias-variance dial · metrics & weighting · **distance concentration** · spatial trees · KNN
regression · **the Cover & Hart bound verified numerically**) → Part 2 wine worked example
→ **Part 3 the production objection** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **The scaling trap:** wine feature ranges span **2,645×**; KNN raw **0.6802** →
  StandardScaler **0.9717**, while a random forest on the same raw features scores 0.9775.
  Proline alone holds **99.8%** of the unscaled variance — the raw model is a one-feature
  model in a thirteen-feature costume, and nothing warns you.
- **Distance concentration measured**, 500 uniform points: spread (max−min)/min falls
  **615.8 → 0.104** from d=1 to d=1000; contrast (std/mean) **0.614 → 0.017**. An L1 column
  was added so the "Manhattan concentrates more slowly" claim is measured, not asserted
  (**0.124 vs 0.104** at d=1000).
- **The practical curse:** holding 5 informative features fixed and adding noise columns,
  KNN falls **0.9700 → 0.7133** while a random forest only moves 0.9625 → 0.9458.
- **Spatial trees stop helping:** trees win only at d=2; from d=5 brute force wins and the
  gap widens to **33×** by d=100. sklearn's `algorithm="auto"` rule was read from source and
  is exact: **more than 15 features → brute force** (also when k ≥ n/2).
- **Cover & Hart verified:** Bayes error 0.1587, bound 0.3173; 1-NN settles at **0.2249** at
  n=80,000 — inside the bound, nearer R* than 2R*. k=15 lands at 0.1712, near R* itself.
- **KNN regression cannot extrapolate:** trained on x∈[0,10], predictions at x=15 and x=25
  are the identical flat value (~22.94) against truths of 33 and 53.
- **Inference cost is linear in n:** predict time 0.0035s → 0.2616s and memory 0.2 → 30.5 MB
  as the training set grows 1k → 200k, while fit time stays ~0.

**Findings that changed the prose** (result kept, prose rewritten to match):

1. **The tuned KNN does not win.** Logistic regression beats default scaled KNN (0.9775 vs
   0.9553) in §2.2, and beats the *tuned* KNN on test (1.0000 vs 0.9778) in §2.5. §2.2 now
   says so explicitly rather than implying KNN wins by the end.
2. **The k sweep found nothing.** All **9 of 9** values of k are within one standard deviation
   of the best, and 3 settings tie *exactly*. §2.5 was rewritten from "anything between 3 and
   21 is fine" into a demonstration that the search proved k does not matter here — with the
   arithmetic (one wine = 0.037 of a fold score, larger than the whole table's spread).
   The one column that *is* informative: every tied setting uses `p=1`.
3. **k=1 loses to the do-nothing baseline** on the imbalanced demo (0.9687 vs 0.9747) while
   having the best minority recall (0.2895). An earlier draft claimed every KNN beat the
   baseline; §3.3 now uses the contradiction as the point.

**Library note:** `load_digits` emits a NumPy 2.5 `DeprecationWarning` from inside sklearn 1.9
(in-place array reshape). Suppressed narrowly around the Part 5 catalogue loop with the reason
stated in a comment — there is nothing to fix on our side.

**(original brief follows)**

- **Unique theory:** lazy learning (no training); distance metrics; **the scaling trap**
  quantified; k as bias-variance; the curse of dimensionality *demonstrated* (distance
  concentration), not just stated; KD-tree/ball-tree and where they stop helping.
- **Worked example:** `load_wine` ✅ — mixed feature scales make the collapse dramatic.
- **Must cover:** uniform vs distance weighting; KNN regression too; memory/latency at
  inference is the real production objection.
- **Papers:** Cover & Hart (1967) *Nearest Neighbor Pattern Classification*;
  Beyer et al. (1999) *When Is "Nearest Neighbor" Meaningful?*

---

### NB-08 — Naive Bayes ✅ COMPLETE
61 cells (30 code). Verified: structure clean, all 30 cells run under warnings-as-errors,
every printed number audited. **Passed the full verification on the first build.**

**Structure as built:** Part 1 theory (Bayes' rule → classifier · **the naive assumption
measured** · log space & underflow · smoothing · from scratch · the four variants · **why a
false assumption still works** · the prior) → Part 2 20 Newsgroups worked example → **Part 3
the probability problem** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **The assumption measured failing:** within the hockey class, "goal"+"scored" co-occur
  **6.03×** more than independence predicts; every pair tested exceeds 1.0.
- **Underflow:** a product of 0.01s hits exactly 0.0 after **162 factors**. A 200-word document
  has ~200.
- **alpha=0:** **39.6%** of the log-probability table becomes −inf, accuracy collapses
  0.94 → **0.6935**, log-loss infinite. (Needs `force_alpha=True` *and* a suppressed
  RuntimeWarning — sklearn makes you ask twice.)
- **From scratch == sklearn:** identical predictions, log-likelihood diff **0.00e+00**.
- **Variants:** continuous data — GaussianNB 0.9385, MultinomialNB 0.8981, **BernoulliNB
  0.6274** (binarises at 0, so all-positive features become all-ones).
- **The centrepiece — duplicating every feature k times** adds no information: accuracy
  0.9407 → 0.9393 and AUC 0.9839 → 0.9823 (untouched), while mean |log-odds| goes
  **160.8 → 1608.1** (exactly linear in k) and log-loss **0.5265 → 1.3761**.
- **Overconfidence:** on raw counts **30.1%** of documents score exactly 0.0 or 1.0 in float64;
  log-odds range **−1459 to +12183**; mean |log-odds| rises 16 → 1355 with document length.
- **Leakage:** metadata is worth **0.8349 → 0.6691** (~25% of the honest score).
- **Prior deadness:** on raw counts a 999:1 prior shift flips only **6.8%** of predictions
  (would need ~10^17:1 to move half); on TF-IDF a 9:1 shift flips **31.6%** and costs 26 points.

**Findings that changed the prose** (result kept, prose rewritten to match):

1. **TF-IDF LOSES to raw counts** (0.6691 vs 0.8103) — the opposite of the standard claim.
   Root cause found and measured: `alpha` is an additive **pseudocount**, TF-IDF's median
   column sum is **0.127**, so `alpha=1.0` is ~8× the evidence it is smoothing. At
   `alpha=0.01` the two representations tie (0.8389 vs 0.8375). §2.3 was rewritten into a
   demonstration of the alpha×vectorizer interaction, and **Q8 was rewritten from "why does
   TF-IDF win" to "you changed the feature scale without changing alpha"**.
2. **Brier score rates NB as BETTER calibrated than logistic regression** (0.0477 vs 0.0754)
   while log-loss rates it far worse (0.5265 vs 0.3117). Brier is bounded; log-loss is not.
   §3.1 and Q5 are built around this rather than around the textbook "NB is miscalibrated".
3. **A second signature leak found in alt.atheism**, not just sci.med. Bob Beauchaine's .sig
   (`bobbe`/`beauchaine`/`sank`/`queens`/`bronx`, a song lyric) is 100% precise for the class
   **and appears in 9–10 test documents** — so unlike the sci.med signature (77 train docs,
   **0 test docs**), that one is a genuine train/test leak. §2.6 now contrasts the two.
4. **MultinomialNB beat the linear SVM in §2.5** (0.8375 vs 0.8149). Rather than claim a win,
   §2.5 now says why the table is unfair — NB was tuned, the others were not, on features
   chosen to suit NB — and names it as the standard way "our model wins" tables get built.
5. **ComplementNB reaches 0.8119 in §3.5** against MultinomialNB's 0.6976 and LinearSVC's
   0.8238, at ~1/12 the SVM's fit time — which changes the section's verdict from "NB is only
   a baseline" to "ComplementNB is genuinely competitive on multiclass text".

**Two bugs caught in my own demos during verification:**

- `fetch_20newsgroups` **sorts** the `categories` list, so indexing your own list mislabels
  every class. Caught when `rec.sport.hockey` came back with evidence words *god, jesus,
  church*. Now taught explicitly in §2.2 with a deliberately unsorted list.
- Millisecond-scale fit times are not reproducible (logistic regression measured 84×, 103× and
  133× slower across three runs). All ratios in §3.5 are now computed at runtime and the prose
  asserts only what survives that noise — the same correction NB-06 needed.

**(original brief follows)**

- **Unique theory:** Bayes' rule → the naive conditional-independence assumption; why it still
  ranks correctly while being badly calibrated; Multinomial vs Bernoulli vs Gaussian NB;
  Laplace smoothing; log-space turning products into a linear sum.
- **Worked example:** `fetch_20newsgroups` ✅ with TF-IDF (as in `Supervised_Learning_Practical_v4` §8).
- **Must cover:** `remove=('headers','footers','quotes')` as a leakage story; alpha tuned by
  CV inside the pipeline; class-vs-others evidence words; prior shift at deployment.
- **Papers:** Domingos & Pazzani (1997) on why NB works; Rennie et al. (2003) *Tackling the
  Poor Assumptions of Naive Bayes*.

---

### NB-09 — PCA & Dimensionality Reduction ✅ COMPLETE
57 cells (28 code). Verified: structure clean, all 28 cells run under warnings-as-errors,
every printed number audited.

**Structure as built:** Part 1 theory (the problem · **variance ⇔ reconstruction** · from
scratch by eigendecomposition · **the SVD route and conditioning** · centring & scaling ·
choosing k · what a component *is* · **PCA is unsupervised**) → Part 2 digits worked example
→ **Part 3 the limits** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **The two definitions are one:** variance kept + reconstruction error is **constant to
  4.6e-13** across every k from 1 to 64, and equals the total variance.
- **From scratch == sklearn:** eigenvalues to 8.5e-14, leading 61 components to 8.5e-12 after
  sign alignment. **30 of 61 components had the opposite sign** — sign is arbitrary.
- **Degeneracy taught, not hidden:** digits' 3 all-zero border pixels give 3 zero eigenvalues
  whose eigenvectors are an arbitrary basis, so only 61 of 64 components are comparable.
- **cond(XᵀX) = cond(X)² exactly** (1e3→1e6, 1e6→1e12, 1e8→8.8e15) — the reason every
  library uses SVD rather than eig(cov).
- **Centring:** uncentred SVD's PC1 sits **0.05°** from the direction of the mean.
- **Scaling:** wine raw PC1 holds 99.8% of variance with proline at 96.9% of the loading;
  downstream accuracy **0.9552 → 0.6965** without a scaler.
- **PCA is unsupervised:** a constructed case where PC1 holds **98.9%** of the variance and
  scores **0.5467**, while PC2 (1.1%) scores **1.0000**.
- **PCA is a rotation:** on concentric circles PCA(2) keeps **100%** of the variance and moves
  a linear model from 0.4583 to 0.4617 — nothing. KernelPCA reaches 1.0000.
- **t-SNE trade quantified:** t-SNE keeps **73.2%** of true 10-NN neighbours vs PCA's
  **25.3%**, but is worse globally (Spearman 0.49 vs 0.60), has **no `transform`**, and runs
  200–1500× slower.

**The finding that corrects this brief's own instruction.** The brief said "**PCA inside a
Pipeline** or you leak". Measured on pure noise (labels independent of features, so honest CV
must be 0.50):

| transform | fitted on all | in Pipeline | inflation |
|---|---|---|---|
| **PCA** (unsupervised) | 0.5400 | 0.5550 | **−0.0150** |
| `SelectKBest(f_classif)` (supervised) | 0.7850 | 0.5500 | **+0.2350** |
| LDA (supervised) | 0.6500 | 0.5900 | +0.0600 |

PCA cannot leak label information because it never sees `y`. §3.4 therefore teaches the
*correct* reasons to pipeline it (the fitted rotation must ship; tuning k requires it) and
redirects leakage-hunting to steps that touch `y`. This is a better lesson than the blanket
rule and is now the notebook's most distinctive section.

**Other findings that changed the prose** (result kept, prose rewritten):

1. **Whitening HURTS KNN (0.9526→0.9438) and HELPS logistic regression (0.9631→0.9666)** —
   the exact opposite of the usual "whiten for distance-based methods" advice. §3.5 now
   explains both directions and concludes it is a property of the *data*, not the model.
2. **PCA before KNN on digits neither helps nor hurts** (PCA(29) ties all-64 at 0.9872; k=40
   gains +0.0011) **and is slightly slower**, because fitting the rotation costs more than it
   saves at 64 features. §2.4 and Q7 were rewritten away from the standard "PCA speeds things
   up and denoises" claim.
3. Draft prose claimed "anything from k≈15 upward beats all 64 pixels" — false (k=15 scores
   0.9839 vs 0.9872). Corrected to k≈30, with a note that the grid also tuned `n_neighbors`
   so the comparison is not like-for-like.

**Bugs caught in my own verification code** (all before any notebook cell was written):

- `explained_variance_` uses ddof=1; my reconstruction MSE used ddof=0, so the "kept + lost"
  sum appeared to drift instead of being exactly constant.
- Comparing all 64 components against sklearn's failed at 2.4e-02 because of the degenerate
  zero-eigenvalue subspace — fixed by comparing only well-determined components.
- The first ill-conditioning demo was already at the float64 limit, so cond(XᵀX) could not
  show the squaring; replaced with matrices built to prescribed singular values.
- `np.corrcoef` divides by a zero std for digits' constant border pixels — caught by the
  warnings-as-errors verifier.

**(original brief follows)**

- **Unique theory:** variance maximisation ⇔ reconstruction-error minimisation; eigenvectors
  of the covariance matrix; the SVD route and why it is used in practice; explained-variance
  ratio and the scree plot; PCA is a *rotation*, components are not features.
- **Must cover:** centring and scaling are mandatory; PCA is unsupervised so the top component
  need not be predictive; whitening; `PCA(n_components=0.95)`; **PCA inside a Pipeline** or you
  leak; when to prefer t-SNE/UMAP (visualisation only, never as model input).
- **Worked example:** `load_digits` ✅ reconstruction at varying k — visually compelling.
- **Papers:** Pearson (1901); Hotelling (1933); Tipping & Bishop (1999) probabilistic PCA;
  van der Maaten & Hinton (2008) t-SNE.

---

### NB-10 — K-Means & Clustering ✅ COMPLETE
56 cells (29 code). Verified: structure clean, all 29 cells run under warnings-as-errors,
every printed number audited. **Passed the full verification on the first build.**

**Structure as built:** Part 1 theory (clustering is ill-posed · Lloyd's from scratch ·
**local optima** · k-means++ · **what k-means assumes** · scaling · **choosing k five ways**
· **clusters from noise**) → Part 2 digits with labels hidden → **Part 3 hierarchical /
DBSCAN / GMM** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Headline demonstrations** (verified numbers):

- **Local optima:** 30 runs at `n_init=1` give **21 distinct solutions**, worst **1.71×** the
  best, only **8 of 30** finding the best. k-means++ narrows it to 9 solutions / 1.44×.
- **k-means++ earns its keep as k grows:** at k=5 it is indistinguishable from random init;
  by k=20 the gap is large in both best and worst case.
- **Choosing k, on data with a known answer of 6:** elbow picks 3, silhouette picks 3,
  Davies-Bouldin picks 4, **Calinski-Harabasz and the gap statistic pick 6**. Three of five
  wrong, and they disagree.
- **Clusters from pure noise:** uniform random points score silhouette **0.38-0.42** across
  k=2..8 (real blobs score 0.57). The **gap statistic answered k=1 on 8 of 8** independent
  noise samples, and its VALUE separates structure from noise 1.70 vs 0.03.
- **Digits worked example:** the label-free metrics pick k=15 / k=4 / k=15 — **none finds
  k=10**. Ward hierarchical wins on ARI (0.7940) over GMM (0.7279) and k-means (0.6696), and
  the silhouette column does *not* rank the methods the way ARI does.
- **Single linkage chaining:** solves two moons perfectly (ARI 1.0), then 12 bridging points
  out of 412 collapse it to **−0.0003**.
- **DBSCAN in 64 dimensions fails** — no usable `eps` on digits (all-noise, 25 clusters, or
  one cluster), for NB-07 §1.5's reason.

**The finding that reframes the standard teaching.** The textbook list of k-means failures
(anisotropy, unequal variance, unequal size, non-convexity) is not ranked correctly:

- **Anisotropy barely matters when clusters are separated.** At `cluster_std=0.6` k-means
  scores a perfect **1.0** on sheared clusters; only at 1.5 does the same shear cost ~0.39 ARI.
  The assumptions are only under stress when clusters compete for points.
- **Unequal SIZES is the failure that matters**, and it is invisible: at fixed separation,
  sizes 200/200/200 → ARI 0.93, but 580/15/5 → **0.03** while GMM holds **0.84**. WCSS is a
  sum, so splitting the big cluster beats isolating the small one. Directly relevant to anyone
  clustering to find a rare segment.

**Prose corrected against measured output:**

1. **Ward linkage is NOT tolerant of unequal sizes** — it scored **0.2241**, worse than
   k-means' 0.3272, while average linkage scored 0.8427. Ward minimises within-cluster
   variance, which is k-means' objective by another route, so it inherits the same bias. The
   §3.4 comparison table and Q5 were corrected, and the mechanism is now taught.
2. The DBSCAN `eps` sweep and the digit-fragmentation claim both quoted numbers from a
   different sample size than the notebook uses; both now compute themselves at runtime.

**Bugs caught in my own verification code** (before any cell was written): the gap statistic
appeared to fail on noise (k=2) on a single sample — across 8 samples it is correct 8/8; and
the first shape demos applied `StandardScaler`, which partly un-sheared the anisotropic case
and hid the effect being measured.

**(original brief follows)**

Folds in the extras from `Unsupervised_Learning_Practical_v4.ipynb`.
- **Unique theory:** Lloyd's algorithm; the objective (within-cluster sum of squares) and why
  it only finds a local optimum; k-means++ initialisation; choosing k (elbow, silhouette, gap)
  and why all three are unsatisfying; assumes spherical equal-variance clusters.
- **Also cover:** Hierarchical + dendrograms, DBSCAN (density, noise points, no k needed),
  GMM (soft assignment, BIC). One notebook, four methods, compared on the same data.
- **Must cover:** evaluation without labels is genuinely hard; clusters always come back even
  from pure noise.
- **Papers:** MacQueen (1967); Arthur & Vassilvitskii (2007) k-means++; Ester et al. (1996) DBSCAN.

---

### NB-11 — Imbalanced Classification ✅ COMPLETE
46 cells (22 code). Verified: structure clean, all 22 cells run under warnings-as-errors,
every printed number audited.

**Structure as built:** Part 1 theory (why accuracy lies · **PR vs ROC** · the three levers ·
**SMOTE from scratch** · where interpolation goes wrong · **threshold moving** · **does
resampling help?** · calibration damage) → Part 2 mammography worked example → **Part 3 the
leak + cost-based thresholds** → Part 4 questions → Part 5 datasets → Part 6 papers.

**Extra dependency added:** `imbalanced-learn` 0.14.2. The install cell handles it, and SMOTE
is also implemented from scratch in §1.4 so the core lesson does not depend on the library.

**Headline demonstrations** (verified numbers):

- **The leak, and it is the largest in the series.** SMOTE before cross-validation on **pure
  noise** (labels independent of features) gives **ROC-AUC 0.8323** where the truth is 0.50.
  Inside an `imblearn` pipeline: 0.4948. Every sampler fabricates 0.20–0.34 of ROC-AUC.
- **PR vs ROC on one fixed signal**, subsampling only the positives: ROC-AUC stays flat
  (0.8695 → 0.8437 from 50% to 1% minority) while PR-AUC collapses **0.8775 → 0.2152**.
- **Resampling does not improve ranking.** 12 configurations across dimensionality, imbalance
  and separation: SMOTE reduced PR-AUC in **11**, mean **−0.0525**; the one improvement was
  +0.0029. Reproduced on real mammography data.
- **Threshold tuning beats it, free.** Untouched model + tuned threshold: **F1 0.1341** vs
  SMOTE's 0.0581 and class_weight's 0.0583, both at threshold 0.5.
- **Calibration destroyed:** mean predicted probability 0.0168 (true rate 0.0160) → 0.39/0.37/
  0.41 under class weights / SMOTE / undersampling; Brier 0.0157 → ~0.20.
- **Cost-based thresholds** on mammography, with the honest finding that the empirical optimum
  and Elkan's C_FP/(C_FP+C_FN) formula disagree because the model is not perfectly calibrated,
  and that the cost curve is flat near its minimum.

**The finding that corrects this brief.** The brief said "SMOTE on high-dimensional or
categorical data is usually a mistake." Measured, the categorical failure is **conditional and
often absent**: with one categorical column and 3 numeric ones, **0%** of synthetic values are
invalid, because same-category points are nearer so interpolation returns the category
unchanged (100% same-category neighbours). It breaks when the column is a *small share of the
distance* — 29.6% invalid with 30 numeric columns, **92.8%** with 50 levels and 30 numeric.
§1.5 and Q4 now teach the mechanism rather than the slogan. The high-dimensional claim was
also not supported: SMOTE hurt *more* at 10 features than at 1,000.

**A precision issue caught in my own headline.** The PR-AUC "inflation" of +0.70 in the leak
demo partly reflects a **baseline shift** — resampling makes the set 50% positive, so PR-AUC's
random baseline moves from 0.043 to 0.50. ROC-AUC has a 0.50 baseline at any balance, so §3.1
now compares samplers on ROC-AUC and states the distinction explicitly. The leak is unambiguous
either way, but the original framing would not have survived a sharp reader.

**Datasets rejected during verification:** `kddcup99` (subset SA) is too easy — every method
scores PR-AUC ~0.99, so there is nothing to fix. Settled on imbalanced-learn's `mammography`
(11,183 × 6, 2.3% positive), which is genuinely hard (PR-AUC 0.61–0.75) and carries a real
cost asymmetry.

**Library gotchas found:** sklearn's built-in `"f1"`/`"precision"` scorers raise
`UndefinedMetricWarning` under warnings-as-errors when a model predicts no positives — the
notebook defines zero-division-safe scorers once and uses them throughout. And in pandas 3,
`.astype(str)` on a bytes column **decodes** rather than repr-ing it, so comparing against
`"b'normal.'"` silently matches nothing.

**(original brief follows)**

Cross-cutting — build after NB-02..05 so it can reference them.
- **Unique content:** why accuracy is a lie; resampling (random over/under, SMOTE and its
  failure modes); class weights; threshold moving; cost-sensitive learning from a real cost
  matrix; PR-AUC vs ROC-AUC on heavy imbalance; calibration after reweighting.
- **Must cover:** **resample inside the CV fold only** — the single most common leak in this
  topic; SMOTE on high-dimensional or categorical data is usually a mistake.
- **Papers:** Chawla et al. (2002) SMOTE; Saito & Rehmsmeier (2015) PR vs ROC.
- **Extra deps:** `imbalanced-learn`.

---

### NB-12 — Explainable AI ⬜
Cross-cutting — build after the model notebooks.
- **Unique content:** global vs local explanation; permutation importance; partial dependence
  and ICE; **SHAP** (Shapley values from game theory, the additivity axiom, `TreeExplainer`);
  LIME and its instability; surrogate models; counterfactuals.
- **Must cover:** importance ≠ causation (NB-01 Q10's omitted-variable argument);
  explanation methods disagree with each other, and what to do about that;
  correlated features break both permutation importance and SHAP's independence assumption.
- **Papers:** Lundberg & Lee (2017) SHAP; Ribeiro et al. (2016) LIME;
  Rudin (2019) *Stop Explaining Black Box Models…* (essential counterpoint).
- **Extra deps:** `shap`.

---

### NB-13 — Time Series Forecasting ⬜
- **Unique theory:** supervised framing (lag features, rolling windows, horizons); why a random
  split is *leakage*; `TimeSeriesSplit` / walk-forward validation; stationarity, trend,
  seasonality; the naive and seasonal-naive baselines you must beat; **trees cannot
  extrapolate a trend**.
- **Worked example:** ✅ `fetch_openml("Bike_Sharing_Demand", version=2)`.
- **Must cover:** cyclical encoding (sin/cos); horizon ≠ 1 changes everything; MASE/sMAPE;
  classical baselines (ARIMA/ETS) as the honest comparison.
- **Traps:** the random split (quantify the inflated score once, then never again);
  target leakage via a rolling mean computed over the full series.
- **Papers:** Hyndman & Athanasopoulos *FPP3* (free online); Bergmeir & Benítez (2012) on CV
  for time series.

---

### NB-14 — Recommender Systems ⬜
- **Unique theory:** the user-item matrix and its sparsity; content-based vs collaborative;
  user-user / item-item neighbourhood methods; matrix factorisation (SVD/ALS) and implicit
  feedback; the cold-start problem.
- **Must cover:** ranking metrics not RMSE (precision@k, recall@k, NDCG, MAP); splitting by
  *user* or by *time*, never randomly by row; popularity bias and the feedback loop.
- **Worked example:** MovieLens 100k *(candidate — verify a loader; may need a download)*.
- **Papers:** Koren, Bell & Volinsky (2009) *Matrix Factorization Techniques*;
  Hu, Koren & Volinsky (2008) implicit feedback.
- **Extra deps:** possibly `implicit` or `surprise` — prefer a from-scratch ALS/SVD to avoid.

---

### NB-15 — Anomaly Detection ⬜
- **Unique theory:** unsupervised vs semi-supervised vs supervised framing; why "anomaly" is
  not a class; statistical thresholds (z-score, IQR, Mahalanobis); Isolation Forest (isolation
  depth); One-Class SVM; LOF (local density); autoencoder reconstruction error.
- **Must cover:** contamination is a *guess* you must justify; evaluation with almost no labels;
  precision@k as the practical metric; drift vs anomaly.
- **Worked example:** credit-card-fraud style imbalanced data; Isolation Forest as in
  `Unsupervised_Learning_Practical_v4.ipynb` §7.
- **Papers:** Liu, Ting & Zhou (2008) Isolation Forest; Breunig et al. (2000) LOF;
  Schölkopf et al. (2001) One-Class SVM.

---

## 9. Status log

Append a dated entry every session. Newest first.

### 2026-09-07 (NB-11)
- **NB-11 Imbalanced Classification: COMPLETE.** 46 cells (22 code, 24 markdown). Verified:
  structure clean, all 22 cells run under warnings-as-errors, every printed number audited.
- Adds **`imbalanced-learn`** as the series' second extra dependency (after catboost in NB-05).
  SMOTE is also written from scratch in §1.4, so nothing essential depends on the library.
- **The notebook's conclusion contradicts the standard advice**, and it is measured rather than
  asserted: across 12 configurations SMOTE reduced PR-AUC in 11, threshold tuning beat every
  resampling method on F1, and resampling moved the mean predicted probability from 0.017 to
  0.39. This matches Elor & Averbuch-Elor (2022), which is cited as the "read this one" paper.
- **The leak demo is the largest in the series:** SMOTE before CV on pure noise gives ROC-AUC
  **0.8323** against a truth of 0.50.
- **Two corrections to my own work during the audit**, both worth recording:
  - The brief's claim that SMOTE breaks on categorical data is **conditional**. It does not
    break at all when the categorical column dominates the distance (0% invalid values), and
    breaks badly when it does not (92.8%). §1.5 now teaches the mechanism.
  - My headline over-claimed: part of the PR-AUC "inflation" in the leak demo is a **baseline
    shift**, since resampling makes the evaluation set 50% positive. §3.1 was rewritten to
    compare samplers on ROC-AUC, which has a fixed 0.50 baseline, and to state the distinction.
- **Dataset rejected:** `kddcup99` proved too easy (PR-AUC ~0.99 for everything). Switched to
  `mammography`, which is hard and has a genuine cost asymmetry for §3.2.
- **Two library gotchas added to §7's table:** sklearn's built-in `f1`/`precision` scorers warn
  when nothing is predicted positive (fatal under warnings-as-errors), and pandas 3's
  `.astype(str)` decodes bytes rather than repr-ing them.

### 2026-09-07 (NB-10)
- **NB-10 K-Means & Clustering: COMPLETE.** 56 cells (29 code, 27 markdown). Verified:
  structure clean, all 29 cells run under warnings-as-errors, every printed number audited.
  Passed the full verification on the **first** build — the third notebook to do so.
- Written around the fact that clustering has **no ground truth**, so the notebook spends more
  effort on evaluation than on the algorithm. Part 2 deliberately withholds the digit labels
  until §2.4 so the reader sees which decisions the label-free metrics could actually support.
- **Two findings reframe the standard teaching**, both measured:
  - The textbook list of k-means failures is mis-ranked. **Anisotropy barely matters** when
    clusters are separated (perfect ARI on sheared clusters at `cluster_std=0.6`), while
    **unequal cluster sizes** collapse it from 0.93 to **0.03** at fixed separation. The
    second failure is the one that matters and the one nobody demonstrates.
  - **Ward linkage inherits k-means' bias**, because it minimises within-cluster variance —
    k-means' objective by another route. Measured at ARI 0.2241 on unequal sizes against
    k-means' 0.3272 and average linkage's 0.8427. My own §3.4 comparison table had called
    hierarchical "tolerant"; corrected, with the mechanism now explained in §3.4 and Q5.
- **The gap statistic is the notebook's practical takeaway.** It is the only one of five
  methods that can answer "k=1, there are no clusters", and it did so on **8 of 8** noise
  samples where silhouette scored the same noise at 0.42.
- **Bugs in my own verification code again** — a single-sample gap-statistic misfire that
  looked like a real failure until repeated across samples, and a `StandardScaler` in the shape
  demos that partly un-sheared the data and hid the effect being measured.

### 2026-09-07 (NB-09)
- **NB-09 PCA & Dimensionality Reduction: COMPLETE.** 57 cells (28 code, 29 markdown).
  Verified: structure clean, all 28 cells run under warnings-as-errors, every printed number
  audited.
- Built verification-first again. That paid off unusually well here: **four bugs were in my
  own verification code**, not the notebook (ddof mismatch, degenerate-eigenvector comparison,
  an ill-conditioning demo already at the float64 limit, and a corrcoef divide-by-zero). All
  four would have become wrong prose if the demos had been written straight into cells.
- **The headline finding contradicts this plan's own NB-09 brief.** The brief said "PCA inside
  a Pipeline **or you leak**". On pure noise, fitting PCA outside the CV loop inflates accuracy
  by **−0.015** — nothing — while `SelectKBest` inflates by **+0.235** and LDA by +0.060. PCA
  never sees `y`, so it has no label information to smuggle. §3.4 now teaches the correct
  reasons to pipeline PCA and points leakage-hunting at supervised steps instead. The brief
  above has been annotated rather than silently corrected.
- **Three more prose claims were contradicted and rewritten**, the sharpest being that
  **whitening helps logistic regression and hurts KNN** — the reverse of the standard advice.
- Also rewrote the "PCA denoises and speeds things up" framing: on digits it does neither
  (ties on accuracy, marginally slower), which is a more useful thing for a reader to know
  than a repeated slogan.

### 2026-09-06 (documentation refresh, second pass)
- Audited the plan and root README again after NB-08 rather than only bumping the counters.
  Five items were stale or self-contradictory:
  - **The file tree ended at NB-07** and did not list `tools/check_links.py`.
  - **§5 still targeted "~100 cells"** for post-NB-00 notebooks. Measured across NB-02..08 the
    real figure is 44–62, averaging ~52. Added a note not to pad to hit a count.
  - **§5 documented only NB-01's part numbering** (7/8/9 for questions/datasets/papers) while
    every notebook from NB-02 on uses 4/5/6. A fresh session following §5 would have built the
    wrong shape. The actual topic-notebook layout is now a table of its own.
  - **§6 rule 10 said "ship with cleared outputs"** while §10 recorded the opposite decision.
    Rule 10 now states the ship-with-outputs convention and clarifies that the verifier
    enforces *consistency*, not the choice.
  - The folder README described Part 6 as containing "how to read a paper", which no
    topic notebook has — that was NB-01's Part 9.
- Added to §7: the dataset-download/caching note (NB-08 fetches ~14 MB), a one-liner for
  auditing which notebooks still lack stored outputs, and a **library-gotchas table**
  consolidating the ten deprecations and API traps paid for across NB-00..08, so they are not
  rediscovered one notebook at a time.

### 2026-09-06 (NB-08)
- **NB-08 Naive Bayes: COMPLETE.** 61 cells (30 code, 31 markdown). Verified: structure clean,
  all 30 cells run under warnings-as-errors, every printed number audited. Passed the full
  verification on the **first** build — the second notebook in the series to do so.
- Built verification-first: every risky demo was run in the scratchpad *before* any generator
  cell was written. That is what surfaced the TF-IDF and Brier findings early enough to shape
  the notebook's structure rather than force a rewrite.
- **Five prose claims were contradicted by measured output and rewritten** (detail in the NB-08
  brief). The two that changed the notebook's shape:
  - **TF-IDF scored 14 points WORSE than raw counts.** Chasing it down produced the best
    section in the notebook: `alpha` is an additive pseudocount, TF-IDF column sums are ~0.13,
    so the default `alpha=1.0` swamps the data. At `alpha=0.01` the gap disappears. Q8 was
    rewritten from the textbook question to this one.
  - **Brier score reported NB as better calibrated than logistic regression** while log-loss
    reported it as twice as bad. §3.1 now teaches *which metric detects overconfidence* rather
    than merely asserting NB is overconfident.
- **A second leak found by reading the model's own evidence words** — alt.atheism is detected
  by one poster's signature, and unlike the well-known sci.med one, it reaches the test set.
- **Two bugs in my own verification code**, both now taught in the notebook: `fetch_20newsgroups`
  sorts `categories` (caught when hockey's top words were *god, jesus, church*), and
  millisecond fit-time ratios are not reproducible across runs.

### 2026-09-06 (documentation refresh)
- Audited this plan and the root README for content that had gone stale as the series grew,
  rather than only bumping the NB-07 status. Five real problems found:
  - **The file tree still ended at NB-06** — `knn_zero_to_hero.ipynb` was missing from it.
  - **The “~150 cells each ≈ 2,300 total” projection was obsolete.** It predates NB-00.
    Post-NB-00 topic notebooks measure 44–62 cells (~51 average), so the real projection is
    **~948**, of which 540 are built. §2's per-notebook target was corrected the same way.
  - **The link checker was inlined in §7 as a bash heredoc containing a backslash-heavy
    regex** — which is exactly the mangling hazard documented in the subsection immediately
    below it. Promoted to `tools/check_links.py` and the heredoc removed.
  - **§10 still said “next up: NB-02”** and claimed the outputs question was settled.
  - **The root README listed only the tracker notebooks**, omitting the four practical
    notebooks the plan itself mines for material; tracker 4 was also out of order.
- **Discrepancy worth recording:** the outputs convention is not being met. Only NB-00 (40/40
  code cells) and NB-01 (74/77) carry stored outputs. **NB-02 through NB-07 carry none**, so
  on GitHub they render as code with no results — which undermines the series' central claim
  that every number is verified, for anyone browsing rather than running. Now tracked as an
  open item in §10. They all pass `--run`; this needs a save, not a fix.
- Added `tools/check_links.py` (37 links, 0 broken) and listed both tools in the root README.

### 2026-09-06 (NB-07)
- **NB-07 K-Nearest Neighbors: COMPLETE.** 52 cells (24 code, 28 markdown). Verified:
  structure clean, all 24 cells run under warnings-as-errors, every printed number audited.
- Written against **NB-06** as the foil — the other distance-based model, so it inherits the
  scaling dependency and the dimensionality problem, and §1.5 is the payoff section.
- **Three prose claims were contradicted by the measured output and rewritten** (see the
  NB-07 brief for detail): logistic regression beats the tuned KNN on wine; the k sweep
  found *no* distinguishable value of k rather than a comfortable plateau; and k=1 scores
  *below* the majority baseline on the imbalanced demo while having the best recall. All
  three are now the teaching point of their section instead of being smoothed over.
- **Two claims were unsupported and are now measured rather than asserted:** an L1 column was
  added to the distance-concentration table so "Manhattan degrades more gracefully" is a
  result (0.124 vs 0.104 at d=1000), and sklearn's `algorithm="auto"` rule was read from
  source — it is exactly `n_features > 15`, not a vague heuristic.
- **Build-time bug caught by the verifier:** `k=151` in the large-k sweep raises `ValueError`
  under 5-fold CV, because each fold trains on only ~142 of the 178 wines. Capped at k=101,
  and the ceiling (k cannot exceed the fitted sample count) is now taught in §1.4.
- **Library note:** `load_digits` triggers a NumPy 2.5 `DeprecationWarning` inside sklearn 1.9;
  suppressed narrowly around one loop with the reason in a comment.

### 2026-09-06 (NB-06)
- **NB-06 Support Vector Machines: COMPLETE.** 50 cells (28 code, 22 markdown). Verified:
  structure clean, all 28 cells run under warnings-as-errors, every printed number audited.
- Written against **NB-02** as the foil — both draw linear boundaries, and §1.4 contrasts
  hinge loss with log-loss to explain every behavioural difference between them.
- **Two library facts discovered during verification, both now taught rather than hidden:**
  - `SVC(probability=True)` is **deprecated in sklearn 1.9**, removal in 1.11 — caught because
    the verifier treats `FutureWarning` as an error. §3.2 and Q9 rewritten around
    `CalibratedClassifierCV(SVC(), ensemble=False)`, and the new API turns out to fix the old
    one's `predict`/`predict_proba` inconsistency, which improved the section.
  - `Nystroem`/`RBFSampler` default to `gamma=1.0` rather than SVC's `"scale"`. The
    kernel-approximation table originally showed RBFSampler at **0.5150 (chance)** for this
    reason; now both the correct and the default-gamma rows are shown, with the explanation.
- **Other corrections:** the fit-time chart claimed linear models "do not" scale super-linearly
  while the measured LinearSVC exponent was inflated by millisecond-scale overheads — now both
  exponents are computed and the caveat stated, and the 500k extrapolation is calculated at
  runtime rather than hard-coded.

### 2026-09-06 (NB-05)
- **NB-05 Gradient Boosting: COMPLETE.** 46 cells (25 code, 21 markdown). Passed the full
  verification on the **first** build — the first notebook in the series to do so.
- Built as the deliberate counterpart to NB-04: the front matter states the bagging/boosting
  contrast up front, and §1.5 and §1.6 each measure it directly on identical data.
- **Corrections made after auditing the output** (all fixed):
  - **Part 3's tuning did not work.** CV said +0.0050; the CV std was 0.0077; the test set said
    −0.0010. The section now says so explicitly and uses it to demonstrate Q12 rather than
    pretending tuning won. Best teaching moment in the notebook.
  - Early stopping improved log-loss hugely but left AUC flat-to-marginally-lower. Added the
    explanation: overfitting in boosting destroys **calibration** before it degrades
    **ranking**, so monitoring AUC alone will miss it.
  - "100× faster" in two places → measured speedups ranged 17× (CatBoost) to 139× (LightGBM);
    reworded to "one to two orders of magnitude".
  - The `num_leaves` discussion said "turn it down first" immediately after a table where
    turning it down cost 0.017 AUC. Clarified that it is the lever when *overfitting*, and
    that the transferable point is *which* knob holds capacity in LightGBM.
- Deliberately **not** bit-matching sklearn in §1.2 (its per-stage RNG differs). Instead the
  additive structure is proved exactly using sklearn's own trees — a stronger demonstration
  than an approximate reimplementation.

### 2026-09-06 (folder reorganisation)
- **Moved all five notebooks into `ML-Zero-to-Hero/`** and added a reader-facing
  `ML-Zero-to-Hero/README.md` with the reading order, suggested paths by goal, the shared
  notebook structure, and what "verified" means.
- **Fixed the relative links the move broke.** Three notebooks linked to
  `ZERO_TO_HERO_PLAN.md` and now use `../ZERO_TO_HERO_PLAN.md`. Two plain-text filename
  mentions were upgraded to real links while there. **All 11 relative links verified to
  resolve**; a reusable link-checker is now in §7.
- Updated this plan (all paths prefixed, new "Where the files live" and "Reading order"
  sections) and the root `README.md`.
- **Convention recorded:** two READMEs with two audiences — the folder README is for the
  student, this file is for whoever is building. Update both when a notebook lands.

### 2026-09-06 (NB-04)
- **NB-04 Random Forest & Bagging: COMPLETE.** 44 cells (26 code, 18 markdown). Verified:
  structure clean, all 26 cells run under warnings-as-errors, every printed number audited.
- Built as the **payoff for NB-03**: opens by restating NB-03 Part 3's measurement (high
  variance, low bias, roughly independent errors) and derives bagging from it.
- Part 1.2 introduces the variance formula $\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$ and then
  **every later section refers back to it** — decorrelation attacks ρ, more trees attacks the
  second term, pruning the base learner attacks the wrong thing. Worth reusing as a spine.
- **Bugs caught during verification** (all fixed):
  - `oob_score=True` at `n_estimators=10` raises sklearn's "too few trees" `UserWarning`.
    Captured and reported as a table column — the warning is a real signal here, since Part 1.4
    is *about* small-forest OOB being unreliable.
  - Wrote that bagging "does little for the stump". It actually gained **+0.08 AUC**.
    Rewritten around Breiman's real criterion — **stability**, not bias — with logistic
    regression (0.8936 → 0.8934) as the clean null case, and the stump reframed as "helped,
    but still capped by bias".
  - The drop-column table showed pure `noise` losing **more** (0.0071) than a real signal
    (0.0065). Rather than hide it, added a note that single-feature drop-column differences of
    that size are inside the refit noise floor.
  - Hard-coded "~0.22 AUC" for the group importance (actual 0.2942) → now computed at runtime.
  - Challenge 3's argmax claim was too strong — several `max_features` settings are within a
    few thousandths. Reworded so the robust claim is the *shape* (both extremes lose), not the
    exact winner.
  - Printed OOB accuracy directly above CV ROC-AUC without labelling the metric change.

### 2026-09-06 (NB-03)
- **NB-03 Decision Trees: COMPLETE.** 51 cells (28 code, 23 markdown). Verified: structure
  clean, all 28 cells run under warnings-as-errors, every printed number audited.
- Deliberately built as the **setup for NB-04** — Part 3 measures tree instability (5
  different root splits across 60 bootstraps, equal accuracy) and then shows averaging fixing
  it, so bagging arrives as a conclusion rather than a new topic.
- **Bugs caught during verification** (all fixed):
  - Part 3 fitted on numpy arrays but scored on a DataFrame → feature-name `UserWarning`.
    Worth remembering: sklearn warns on that mismatch in **both** directions.
  - Wrote "fewer leaves, **same or better** accuracy" for the pruning result. The pruned tree
    actually scored **worse** on the test set (0.9091 vs 0.9231) while CV preferred it.
    Rewritten honestly — the gap is 2 patients out of 143, so the real lesson is about
    test-set noise and not over-reading small differences. Better teaching than the original.
  - `entropy()` printed `-0.0000` for a pure node (negative zero).
  - The Part 1.1 ASCII schematic used invented patient counts that looked like real output
    from this dataset; relabelled as a schematic with the real tree printed below it.
  - The from-scratch tree printer did not label which child was the `yes` branch.
  - Left a garbage placeholder lambda in Challenge 1 while drafting — caught before build.
- Also documented in the notebook: `export_text` showing splits whose children predict the
  **same class** (they change `predict_proba`, not `predict`) and `truncated branch of depth
  N` being a display limit, not the end of the tree.

### 2026-09-06 (latest)
- **NB-02 Logistic Regression: COMPLETE.** 62 cells (35 code, 27 markdown). Verified:
  structure clean, all 35 cells run under warnings-as-errors, every printed number audited
  against its surrounding prose.
- **First notebook built on the post-NB-00 shape** — opens with a prerequisite pointer to
  Foundations and omits Parts 2/3/5. Came in at 62 cells vs NB-01's 157, so the shared-
  foundations decision is paying off roughly as predicted.
- **Bugs caught during verification** (all fixed):
  - `load_digits` triggers a NumPy 2.5 `DeprecationWarning` inside sklearn 1.9 → multiclass
    demo moved to `load_wine`; the Part 5 catalogue suppresses it deliberately with a comment.
  - Planned to claim "OvR probabilities don't sum to 1" — sklearn **renormalises** them, so
    the demo now shows the raw per-estimator outputs (which sum to 1.0016, 1.0282, 0.9957).
  - Wrote "essentially a tie" for the LR-vs-tree comparison; the tree actually **lost by
    0.096 AUC**. Rewritten — and it makes a better lesson than the tie would have.
  - "catches almost no churners at 0.5" → it catches **exactly zero**. Strengthened.
  - Hard-coded "~4x" for the calibration damage (actual 5.8×) → now computed at runtime.
  - A weak compounding example (10 × 1.3% ≈ 13% vs 14.3%) → replaced with support calls,
    where 3 × 39% = 118% vs the true 170%.
  - "+0.19" probability change → actual +0.168.
  - Claimed the empirical cost-optimal threshold "lands near" the theoretical one; 0.033 vs
    0.054 is the same region but not close. Now explained honestly (flat cost curve, ~80
    validation positives, so the argmin is noisy) with a recommendation to prefer the formula.
  - `paperless_billing` (a planted null) came out at odds ratio 0.889, which reads as a real
    11% effect. Turned into an explicit **noise floor** teaching point rather than glossed as
    "near zero".
- **Fixed a false positive in `tools/verify_notebook.py`.** It compared the *count* of cells
  with outputs against the count with an `execution_count`, and failed NB-01 once the
  notebook had actually been run (77 executed, 74 produced output). A cell can legitimately
  run and print nothing. The check now tests the correct one-directional invariant: a cell
  with **outputs** must have an **execution_count**. Still correctly flags
  `ml_study_tracker_2_classical_ml.ipynb` cell 8.
- **NB-00 and NB-01 now carry outputs** (run by the user in VSCode), so the "ship
  output-free?" open question is effectively answered — they ship with outputs.

### 2026-09-06 (later)
- **NB-00 ML Foundations: COMPLETE.** 78 cells (40 code, 38 markdown), Parts 0–10 +
  Appendix. Verified: structure clean, all 40 code cells run in order under
  warnings-as-errors, every printed number checked against its surrounding prose.
- Covers everything the plan called for, including the gaps NB-01 had: `StratifiedKFold` /
  `GroupShuffleSplit` / `TimeSeriesSplit`, `make_column_selector`,
  `set_config(transform_output="pandas")`, classification metrics, ROC vs PR on imbalanced
  data, cost-based thresholding, `TunedThresholdClassifierCV`, calibration, randomized /
  halving search, and nested CV.
- **Bugs caught during verification** (all fixed):
  - `make_column_selector(dtype_include=object)` raises `Pandas4Warning` under the pandas 3
    string migration → use `dtype_exclude=np.number`, which is portable across pandas 2/3.
  - `OneHotEncoder` defaults to `sparse_output=True`, which is incompatible with
    `transform_output="pandas"` → kept as a documented gotcha in the notebook.
  - The group-leakage demo originally showed only +0.004 AUC — too weak to teach anything.
    Redesigned so labels are coin flips per patient and features are a patient fingerprint;
    now shows +0.454, with the honest score at chance.
  - The tuning cell took **178 s** (halving over a 960-point grid). Reduced to a 54-point
    grid, all three searches timed; now ~22 s total.
  - A claim that halving "finished faster than the full grid" was false on re-run (timings
    vary). Rewritten so the comparison is *computed at runtime* rather than asserted.
  - `np.float64(...)` reprs leaking into printed dicts; an em-dash inside a `print()` that
    would break on a cp1252 console.
- **Decision recorded:** NB-02 onward should open with a pointer to NB-00 and omit Parts
  2/3/5, targeting ~100 cells instead of 157.

### 2026-09-06
- **NB-01 Linear Regression: COMPLETE.** 157 cells (77 code, 80 markdown). Verified: all 77
  code cells run in order under warnings-as-errors; every prose claim checked against actual
  output; all 27 URLs fetched (24×200, 3×403 = Cloudflare bot-blocking on paywalled
  publishers, already labelled ❌).
  - Parts 5, 6, 8, 9 were added after the initial build (real-world data, uncertainty &
    inference, practice datasets, reading the literature).
  - Bugs caught during verification and fixed: gradient descent diverged (learning rate tuned
    for the wrong data scale); `np.linalg.solve` does **not** raise on a singular matrix;
    `ndarray.ptp()` removed in NumPy 2; DataFrame vs ndarray feature-name warning; degree-15
    polynomial demo numerically pathological; 6 prose claims contradicting real output.
  - **Outstanding:** notebook ships with **no stored outputs** — needs one clean run.
- **Created `tools/verify_notebook.py`** — the reusable quality gate. Confirmed it is not
  vacuous: it correctly flags `ml_study_tracker_2_classical_ml.ipynb`.
- **Cleaned `Supervised_Learning_Practical_v4.ipynb`** — removed 11 edit-history references
  ("the v2 bug", "in v3 we…"), completed the "🧠 Can you answer?" feature (5 of 10 sections
  were missing it; the intro promised all 10), stripped stderr containing absolute
  micromamba paths, renumbered `execution_count` 1–21. Backup was in the session scratchpad
  (now gone); the original is recoverable from git.
- **Fixed the Linear Regression section of `ml_study_tracker_2_classical_ml.ipynb`** — inverted
  residual sign pattern, a residual-mean check that can never fail, collinear toy data in two
  cells, a false ridge claim; broke six run-on bullets into sub-bullets; added a residual plot.
- **Known issue:** `ml_study_tracker_2_classical_ml.ipynb` currently fails structure checks
  (6 cells missing `id`, 1 cell with outputs but no `execution_count`). Also, VSCode stripped
  outputs from 76 of its 77 previously-run cells during this session — recoverable from git
  if wanted.

---

## 10. Open questions for the user

- [x] ~~Build **NB-00 Foundations** first?~~ **Done 2026-09-06.** Through NB-11 as of the
      latest session; next up is **NB-12 Explainable AI**.
- [x] ~~Ship notebooks output-free?~~ **No** — the convention is **ship with outputs**.
- [ ] **Five notebooks still ship without stored outputs.** As of the NB-11 session:

      | carries outputs | none stored |
      |---|---|
      | NB-00 40/40, NB-01 74/77, NB-02 32/35, NB-04 23/26, NB-05 22/25, NB-06 25/28, NB-07 24/24 | **NB-03, NB-08, NB-09, NB-10, NB-11** |

      On GitHub those five render as code with no results, which undercuts the "every number
      is verified" claim for anyone browsing rather than running. All five pass `--run`, so
      this is a **save, not a fix**: open each in VSCode, Run All, save. Worth doing as one
      batch.
      (A count below the code-cell total is normal — a cell that runs and prints nothing
      stores no output. Re-check with the one-liner in §7 rather than assuming.)
- [ ] Restore the stripped outputs in `ml_study_tracker_2_classical_ml.ipynb` from git?
- [x] ~~Is `catboost` / `shap` / `imbalanced-learn` acceptable as extra dependencies?~~
      **Yes, sparingly.** NB-05 uses catboost/xgboost/lightgbm, NB-11 uses `imbalanced-learn`.
      The convention: the install cell handles it, and anything essential is also implemented
      from scratch (NB-11 §1.4 writes SMOTE in four lines) so the lesson survives without it.
      NB-12 will need `shap` on the same terms.
