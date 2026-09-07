# ML: Zero to Hero

A course in notebook form. Each file takes one machine-learning topic from *"I have never
fitted a model"* to *"I can build it, break it, diagnose it and defend it in an interview"*.

Every notebook is standalone and runnable, every code cell is verified to execute cleanly,
and every number quoted in the prose is checked against what the code actually prints.

---

## Start here

**Read `00` first.** It covers the half of the job that is identical for every model —
splitting, leakage, pipelines, messy data, metrics, tuning, shipping. Every other notebook
assumes it and does not repeat it.

After that, `01` and `02` in order. They are the two models everything else is compared
against, and later notebooks refer back to them constantly.

---

## The order

Numbers are the reading order, not the order the topics appear in any syllabus. It is
arranged so each notebook has what it needs from the ones before it.

### Foundations — read first

| # | Notebook | What you get | Status |
|---|---|---|---|
| **00** | [`ml_foundations_zero_to_hero.ipynb`](ml_foundations_zero_to_hero.ipynb) | The shared workflow: train/test splitting, **the five kinds of leakage**, pipelines, missing data, outliers, feature engineering, regression *and* classification metrics, thresholds, calibration, hyperparameter search, shipping and monitoring | ✅ |

### The core four — the models everything else is measured against

| # | Notebook | What you get | Status |
|---|---|---|---|
| **01** | [`linear_regression_zero_to_hero.ipynb`](linear_regression_zero_to_hero.ipynb) | The model fitted three ways (closed form, normal equation, gradient descent), assumptions, Ridge/Lasso, prediction intervals, coefficient inference | ✅ |
| **02** | [`logistic_regression_zero_to_hero.ipynb`](logistic_regression_zero_to_hero.ipynb) | Log-odds, **why squared error is the wrong loss**, odds ratios, thresholds and calibration in depth, multiclass | ✅ |
| **03** | [`decision_trees_zero_to_hero.ipynb`](decision_trees_zero_to_hero.ipynb) | Recursive partitioning, impurity, CART from scratch, why greedy ≠ optimal, pruning, scale invariance, and **the instability that motivates everything after it** | ✅ |
| **04** | [`random_forest_zero_to_hero.ipynb`](random_forest_zero_to_hero.ipynb) | Bootstrap, bagging, **decorrelation**, out-of-bag scoring, and how to read feature importance without fooling yourself | ✅ |

### The rest of the algorithms

NB-05 is the direct sequel to NB-04 — read it next if you work with tabular data. NB-06 and
NB-07 are the two **distance-based** models and are best read as a pair.

| # | Notebook | What you get | Status |
|---|---|---|---|
| **05** | [`gradient_boosting_zero_to_hero.ipynb`](gradient_boosting_zero_to_hero.ipynb) | Boosting as gradient descent in function space, learning rate vs rounds, early stopping, plus XGBoost / LightGBM / CatBoost. Usually the strongest tabular model | ✅ |
| **06** | [`svm_zero_to_hero.ipynb`](svm_zero_to_hero.ipynb) | Maximum margins, support vectors, hinge loss, **the kernel trick** derived and verified, and why SVMs stopped scaling | ✅ |
| **07** | [`knn_zero_to_hero.ipynb`](knn_zero_to_hero.ipynb) | Lazy learning, **the scaling trap** quantified, k as a bias-variance dial, **the curse of dimensionality measured** rather than asserted, the Cover & Hart bound verified, and why "no training time" is a production liability | ✅ |
| **08** | [`naive_bayes_zero_to_hero.ipynb`](naive_bayes_zero_to_hero.ipynb) | Bayes' rule, **the naive assumption measured failing**, log-space underflow, smoothing, the four variants, and **why a false assumption still classifies well** — plus the metric that hides its overconfidence | ✅ |
| **09** | [`pca_zero_to_hero.ipynb`](pca_zero_to_hero.ipynb) | Variance maximisation **shown identical to** reconstruction-error minimisation, the SVD route and why, what a component is and is not, and **which preprocessing actually leaks** | ✅ |
| **10** | [`kmeans_zero_to_hero.ipynb`](kmeans_zero_to_hero.ipynb) | K-Means, hierarchical, DBSCAN and GMM on the same data — **local optima**, the five ways of choosing k that disagree, and **why clustering pure noise still looks like a result** | ✅ |

### Cross-cutting — read after the algorithms

These reference the models above, so they land better once those exist.

| # | Notebook | What you get | Status |
|---|---|---|---|
| **11** | [`imbalanced_classification_zero_to_hero.ipynb`](imbalanced_classification_zero_to_hero.ipynb) | PR-AUC vs ROC-AUC, SMOTE built from scratch and its failure modes, **the resampling leak that fabricates 0.83 ROC-AUC from noise**, and why threshold tuning beats all of it | ✅ |
| **12** | [`explainable_ai_zero_to_hero.ipynb`](explainable_ai_zero_to_hero.ipynb) | Permutation importance, PDP/ICE, **SHAP with its additivity verified**, LIME's instability measured — **how far the methods disagree**, and whether you needed the black box at all | ✅ |

### Applied problem types

| # | Notebook | What you get | Status |
|---|---|---|---|
| **13** | [`time_series_zero_to_hero.ipynb`](time_series_zero_to_hero.ipynb) | Lag features and the supervised framing, **why a random split is leakage** (measured), walk-forward validation, the baselines you must beat, and **why trees cannot forecast a trend** | ✅ |
| **14** | [`recommender_systems_zero_to_hero.ipynb`](recommender_systems_zero_to_hero.ipynb) | Item-item CF and **ALS written from scratch**, **why RMSE ranks the models backwards**, implicit feedback, cold start — and **proof that the popularity baseline only wins because of how the data was collected** | ✅ |
| **15** | [`anomaly_detection_zero_to_hero.ipynb`](anomaly_detection_zero_to_hero.ipynb) | Isolation Forest and LOF **built from scratch**, `contamination` shown to be a threshold rather than a model, precision@k as the metric a team can act on — and **why LOF scores below random on real fraud**, with the fix | ✅ |

**Progress: 16 of 16 — the series is complete.**

---

## Suggested paths

Not everyone should read all sixteen in order.

| If you are… | Read |
|---|---|
| **New to ML** | 00 → 01 → 02 → 03, then stop and do the practice datasets in each before continuing |
| **Preparing for interviews** | Each notebook's **Part 4 (Tough questions)** first. Every question you cannot answer points at the section you need |
| **Working on a real tabular project** | 00 for the workflow → 04 and 05 for the models that will actually win → 11 if your classes are imbalanced |
| **Told to build something interpretable** | 01, 02, 03 — then 12 for the argument about whether "explaining" a black box is good enough |
| **Coming from deep learning** | 00 → 05. Tabular data is still tree country, and Part 6 of NB-04 has the papers on why |
| **Building a recommender or anything that ranks** | 09 for the factorisation idea → 07 for the neighbourhood idea → **14**, whose Part 3 is really about evaluation and applies well beyond recommendation |
| **Hunting rare events** | 11 if you have labels, **15** if you do not — and 15 §2.3 measures how much that difference is worth |

---

## How each notebook is built

Same shape every time, so you always know where to look:

| Part | Contents |
|---|---|
| **0** | Setup — one install cell, one import cell |
| **1** | **Theory from zero** — built up in numbered steps, implemented **from scratch**, checked against scikit-learn in the same cell |
| **2** | **Worked example** — one dataset, end to end, nothing skipped |
| **3** | The topic's signature problem, in depth |
| **4** | **Tough questions** — ~12 with hidden answers, plus 3 coding challenges |
| **5** | **Practice datasets** — 5, ordered by difficulty, each with a brief and the trap it sets. Real data except in NB-14, where MovieLens is currently undownloadable and §1.2 explains what replaced it |
| **6** | **Reading the literature** — two or three papers worth starting with, a table mapping every section to its source, and one "if you read only one" pick |
| — | Appendix — errors specific to that model, and a pre-ship checklist |

Notebooks 01 and 00 predate this template slightly and carry a few extra parts; the shape is
otherwise identical.

---

## Running them

```bash
pip install numpy pandas matplotlib scipy scikit-learn
```

Each notebook's Part 0 installs anything missing, so opening one and running it top to bottom
is enough. A few practice datasets in Part 5 download from OpenML on first use and cache
afterwards.

Everything was verified against **numpy 2.5.2 · pandas 3.0.5 · scikit-learn 1.9.0**.

To check a notebook yourself:

```bash
python ../tools/verify_notebook.py <notebook>.ipynb --run
```

That runs every code cell in order with warnings treated as errors, and checks structure —
cell ids, stray outputs, leaked local paths.

---

## What "verified" means here

Every notebook marked ✅ has had:

- every code cell executed **in order**, with `warnings.simplefilter("error")` — a warning
  fails the build
- every numeric claim in the prose **checked against the actual output**, not written from
  memory
- every URL fetched, and every dataset loader run, before being recommended
- demonstrations tuned until they actually demonstrate the stated lesson — several were
  rebuilt when the first version showed the wrong thing

Where a result came out *contrary* to the point being made, the prose was rewritten to match
the result rather than the result adjusted to match the prose. Those cases are usually the
most instructive parts of the notebook, and they are flagged where they occur.

---

## Also in this folder

This folder is the home for all ML work in the repository, not only the series above. Two
subfolders hold the material the series grew out of. They serve a different purpose and are worth
keeping: the series *teaches* a topic, the trackers *track* what you have covered, and the
practicals are quick worked references.

| Folder | What is in it | When you would open it |
|---|---|---|
| **`trackers/`** | The ML study tracker split into four focused notebooks: foundations & workflow, classical ML, deep learning / GenAI / MLOps, and practical use cases | To tick off what you have covered, or to find the topic checklist behind a notebook above |
| **`practicals/`** | Worked-example notebooks &mdash; supervised, unsupervised, deep learning, and an earlier mixed one. `practicals/archive/` holds superseded versions (v1&ndash;v3) | For a quick worked reference on a technique, without the full theory build-up |

There is also a **`data/`** folder holding the specialty-steel price spreadsheets. No notebook
reads them; they are parked there as raw material.

None of these folders is published to the website; only the 16 series notebooks are. The
notebooks all run the same way: open in Jupyter or VS Code and run top to bottom.

---

The repository root, [`../README.md`](../README.md), lists this series alongside the
other notebook collections here.
