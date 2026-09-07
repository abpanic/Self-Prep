# Self-Prep

Study and interview-prep notebooks for machine learning, software engineering fundamentals, data structures, algorithms, and system-design breadth.

## Contents

### ML: Zero to Hero — complete

A course in notebook form, in **[`ML-Zero-to-Hero/`](ML-Zero-to-Hero/)**. Each notebook takes
one topic from "I have never fitted a model" to "I can build it, break it, diagnose it and
defend it in an interview" — theory built from scratch, a full worked example, hard questions,
practice datasets, and the research papers behind each section.

**All 16 notebooks are complete**, 952 cells in total. Read them in this order — each one
assumes the ones above it, and says so in its own prerequisites line. Both series are also
published as a website (see [Reading it online](#reading-it-online) below), which is easier
to navigate and is searchable.

| # | Notebook | Topic |
|---|---|---|
| 00 | [`ml_foundations_zero_to_hero.ipynb`](ML-Zero-to-Hero/ml_foundations_zero_to_hero.ipynb) | The shared workflow: splitting, pipelines, leakage, cross-validation, metrics |
| 01 | [`linear_regression_zero_to_hero.ipynb`](ML-Zero-to-Hero/linear_regression_zero_to_hero.ipynb) | Least squares from scratch, assumptions, regularisation, inference |
| 02 | [`logistic_regression_zero_to_hero.ipynb`](ML-Zero-to-Hero/logistic_regression_zero_to_hero.ipynb) | Log-odds, maximum likelihood, thresholds, calibration |
| 03 | [`decision_trees_zero_to_hero.ipynb`](ML-Zero-to-Hero/decision_trees_zero_to_hero.ipynb) | Impurity, greedy splitting, pruning, why a single tree overfits |
| 04 | [`random_forest_zero_to_hero.ipynb`](ML-Zero-to-Hero/random_forest_zero_to_hero.ipynb) | Bagging, decorrelation, OOB error, feature importance and its traps |
| 05 | [`gradient_boosting_zero_to_hero.ipynb`](ML-Zero-to-Hero/gradient_boosting_zero_to_hero.ipynb) | Boosting from scratch, then XGBoost / LightGBM / CatBoost compared |
| 06 | [`svm_zero_to_hero.ipynb`](ML-Zero-to-Hero/svm_zero_to_hero.ipynb) | Margins, the dual, the kernel trick, and when kernels stop scaling |
| 07 | [`knn_zero_to_hero.ipynb`](ML-Zero-to-Hero/knn_zero_to_hero.ipynb) | Distance metrics, the scaling trap, distance concentration, ANN search |
| 08 | [`naive_bayes_zero_to_hero.ipynb`](ML-Zero-to-Hero/naive_bayes_zero_to_hero.ipynb) | The independence assumption, log-space, smoothing, text classification |
| 09 | [`pca_zero_to_hero.ipynb`](ML-Zero-to-Hero/pca_zero_to_hero.ipynb) | Variance vs reconstruction, SVD, whitening, and what PCA cannot do |
| 10 | [`kmeans_zero_to_hero.ipynb`](ML-Zero-to-Hero/kmeans_zero_to_hero.ipynb) | Lloyd's algorithm, k-means++, choosing k, hierarchical and DBSCAN |
| 11 | [`imbalanced_classification_zero_to_hero.ipynb`](ML-Zero-to-Hero/imbalanced_classification_zero_to_hero.ipynb) | PR-AUC vs ROC-AUC, SMOTE and its failure modes, threshold moving, costs |
| 12 | [`explainable_ai_zero_to_hero.ipynb`](ML-Zero-to-Hero/explainable_ai_zero_to_hero.ipynb) | Permutation importance, SHAP, LIME, PDP/ICE — and how far they disagree |
| 13 | [`time_series_zero_to_hero.ipynb`](ML-Zero-to-Hero/time_series_zero_to_hero.ipynb) | Lag features, walk-forward validation, MASE, why trees cannot extrapolate |
| 14 | [`recommender_systems_zero_to_hero.ipynb`](ML-Zero-to-Hero/recommender_systems_zero_to_hero.ipynb) | Item-item CF, ALS, ranking metrics, implicit feedback, popularity bias |
| 15 | [`anomaly_detection_zero_to_hero.ipynb`](ML-Zero-to-Hero/anomaly_detection_zero_to_hero.ipynb) | Isolation Forest and LOF from scratch, precision@k, evaluating without labels |

**00 is the one to read first** whatever you are after — the later notebooks assume its
workflow and refer back to it rather than repeating it. After that, 01–03 build the intuition,
04–10 are the models, and 11–15 are the problem types you actually get handed.
[`ML-Zero-to-Hero/README.md`](ML-Zero-to-Hero/README.md) has suggested shorter paths for
specific goals — interview prep, a real tabular project, coming from deep learning.

Every notebook has had all of its code cells executed in order with warnings treated as errors,
and every number quoted in its prose checked against what the code actually printed. Where a
result contradicted the point being made, the prose was rewritten to match the result — those
cases are flagged in the notebooks and are usually the most useful parts.

- `tools/verify_notebook.py` — the quality gate: structure checks plus a full top-to-bottom
  execution with warnings treated as errors
- `tools/check_links.py` — verifies every relative link in the series still resolves

### Reading it online

Both series render to a static website with [Quarto](https://quarto.org), deployed on Vercel.
Quarto reads `.ipynb` natively and **does not re-execute anything** — it uses the outputs
already stored in each notebook — so the build needs no Python, no scikit-learn, no dataset
downloads and (once the DSA series exists) no JDK.

```bash
quarto preview        # local, live-reloading
quarto render         # writes the site to _site/
```

| File | What it does |
|---|---|
| `_quarto.yml` | Site config: which files are published, navbar, per-series sidebars, search |
| `theme.scss` | Light/dark theming, plus the rules that stop fixed-width printed tables from wrapping |
| `index.qmd` | Site landing page |
| `ML-Zero-to-Hero/index.qmd`, `DSA-Zero-to-Hero/index.qmd` | Series landing pages |
| `vercel.json`, `vercel-build.sh` | Vercel build: installs a pinned Quarto, renders to `_site/` |

Only the two Zero-to-Hero series are published. The trackers and practicals inside
`ML-Zero-to-Hero/` are deliberately excluded, because the `render:` globs match only the top level
of each series folder — add them to that list in `_quarto.yml` if that should change.

> **Note on horizontal rules.** Quarto and pandoc read a line of `---` as the start of a YAML
> metadata block, so the notebooks use `***` for section rules instead. It renders identically
> in Jupyter, on GitHub and on the site. Keep using `***` in new notebooks.

### Everything else under `ML-Zero-to-Hero/`

The folder is the home for all ML work, not only the series. Two subfolders hold the material the
series was built from, kept because they serve a different purpose — the series teaches a topic,
the trackers track what you have covered, and the practicals are quick worked references.

```
ML-Zero-to-Hero/
├── *_zero_to_hero.ipynb        <- the 16-notebook series (published to the site)
├── README.md                   <- the reader's guide
├── trackers/                   <- study checklists, 4 notebooks
└── practicals/                 <- worked-example notebooks, 4 + archive/
```

**[`trackers/`](ML-Zero-to-Hero/trackers/)** — the ML study tracker, split into four focused files.
Checklists to mark off, with room for your own notes under each topic.

| Notebook | Covers |
|---|---|
| `ml_study_tracker_1_foundations_workflow.ipynb` | Python for ML, NumPy, Pandas, visualisation, statistics, linear algebra, calculus/optimisation, data cleaning, EDA, feature engineering, splitting, evaluation, cross-validation, tuning, pipelines |
| `ml_study_tracker_2_classical_ml.ipynb` | Linear/logistic regression, KNN, Naive Bayes, trees, forests, gradient boosting, XGBoost/LightGBM/CatBoost, SVMs, K-Means, PCA, imbalanced classification, time series, recommenders, anomaly detection, explainable AI |
| `ml_study_tracker_3_deep_learning_genai_mlops.ipynb` | Neural networks, CNNs, RNNs/LSTMs, transformers, NLP, embeddings, LLMs, RAG, agents, deployment, experiment tracking, model registry, drift detection, retraining |
| `ml_study_tracker_4_practical_ml_use_cases.ipynb` | End-to-end practical use cases |

**[`practicals/`](ML-Zero-to-Hero/practicals/)** — worked-example notebooks that predate the series
and fed material into it.

| Notebook | Covers |
|---|---|
| `Supervised_Learning_Practical_v4.ipynb` | Ten worked sections: linear and logistic regression, KNN, trees, forests, gradient boosting, SVM with PCA, Naive Bayes, time series, cross-validation |
| `Unsupervised_Learning_Practical_v4.ipynb` | K-Means, hierarchical clustering, DBSCAN, GMM, PCA, t-SNE, Isolation Forest |
| `Deep_Learning_Practical_v2.ipynb` | Practical deep learning |
| `Practical-ML.ipynb` | Earlier mixed practical notebook |
| `practicals/archive/` | Superseded versions (v1–v3), kept for reference |

### Everything else under `DSA-Zero-to-Hero/`

Mirrors the ML folder: the series above, plus the material it is being built from.

```
DSA-Zero-to-Hero/
├── DSA_ZERO_TO_HERO_PLAN.md    <- roster, quality bar, per-notebook briefs, status log
├── index.qmd, plan.qmd         <- the site pages
└── trackers/                   <- study checklists, superseded by the series as it lands
    └── archive/                <- the original combined tracker
```

| Notebook | Covers |
|---|---|
| `trackers/core_swe_dsa_tracker_1_data_structures.ipynb` | Arrays/strings, hash tables, stacks/queues, linked lists, trees, BSTs, heaps, graphs, advanced graph concepts, tries, union-find |
| `trackers/core_swe_dsa_tracker_2_algorithms.ipynb` | Complexity, sorting, binary search, recursion, backtracking, sliding window, two pointers, greedy, dynamic programming, graph traversal, shortest paths, topological sort, bit manipulation, problem log |
| `trackers/archive/core_swe_dsa_tracker.ipynb` | The original combined tracker the two above were split from. Kept for reference |

The two split notebooks are the ones to use day to day; they are smaller and easier to navigate.

### Software Engineering Breadth

- `SWE_breadth_topics.ipynb`
  Breadth notebook for software engineering concepts beyond DSA, including distributed systems
  and backend/system-design topics such as caching and consistent hashing. Neither ML nor DSA,
  so it stays at the root.

## How to Use

Open the notebooks in Jupyter, VS Code, or another notebook editor. Use the checklists to track progress, run the examples, and add your own notes or practice solutions under each topic.

Each series folder is self-contained: `ML-Zero-to-Hero/` holds the ML series plus its trackers, practicals and data, and `DSA-Zero-to-Hero/` holds the DSA plan plus its trackers. The split tracker notebooks are the ones to use day to day; the originals they were split from are kept in the `archive/` folders for reference.

## Attribution

Author: `abpanick`

Created and refined with assistance from ChatGPT, Claude, and Perplexity.
