# Self-Prep

Study and interview-prep notebooks for machine learning, software engineering fundamentals, data structures, algorithms, and system-design breadth.

## Contents

### ML: Zero to Hero — complete

A course in notebook form, in **[`ML-Zero-to-Hero/`](ML-Zero-to-Hero/)**. Each notebook takes
one topic from "I have never fitted a model" to "I can build it, break it, diagnose it and
defend it in an interview" — theory built from scratch, a full worked example, hard questions,
practice datasets, and the research papers behind each section.

**All 16 notebooks are complete**, 952 cells in total. Read them in this order — each one
assumes the ones above it, and says so in its own prerequisites line.

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

### Practical ML notebooks

Worked-example notebooks that predate the series above and feed material into it.

- `Supervised_Learning_Practical_v4.ipynb` — ten worked sections: linear and logistic
  regression, KNN, decision trees, random forests, gradient boosting, SVM with PCA, naive
  Bayes, time series, and cross-validation.
- `Unsupervised_Learning_Practical_v4.ipynb` — K-Means, hierarchical clustering, DBSCAN,
  GMM, PCA, t-SNE, and Isolation Forest.
- `Deep_Learning_Practical_v2.ipynb` — practical deep learning.
- `Practical-ML.ipynb` — earlier mixed practical notebook.

### Machine Learning Study Tracker

These notebooks split the original ML tracker into smaller, focused files.

- `ml_study_tracker_1_foundations_workflow.ipynb`  
  ML foundations and workflow: Python for ML, NumPy, Pandas, data visualization, statistics, linear algebra, calculus/optimization, data cleaning, EDA, feature engineering, train/validation/test splitting, model evaluation, cross-validation, hyperparameter tuning, and scikit-learn pipelines.

- `ml_study_tracker_2_classical_ml.ipynb`  
  Classical ML algorithms and advanced ML topics: linear/logistic regression, KNN, Naive Bayes, decision trees, random forests, gradient boosting, XGBoost/LightGBM/CatBoost, SVMs, K-Means, PCA, imbalanced classification, time series, recommender systems, anomaly detection, and explainable AI.

- `ml_study_tracker_3_deep_learning_genai_mlops.ipynb`  
  Deep learning, NLP, GenAI, and MLOps: neural networks, CNNs, RNNs/LSTMs, transformers, NLP basics, embeddings, LLM basics, RAG, AI agents, deployment basics, experiment tracking, model registry, drift detection, and retraining strategy.

- `ml_study_tracker_4_practical_ml_use_cases.ipynb`
  End-to-end practical ML use cases.

### Core SWE / DSA Tracker

- `core_swe_dsa_tracker.ipynb`  
  Original full tracker for core software engineering interview prep, data structures, algorithms, and a problem log.

- `core_swe_dsa_tracker_1_data_structures.ipynb`  
  Split notebook focused on data structures: arrays/strings, hash tables, stacks/queues, linked lists, trees, BSTs, heaps, graphs, advanced graph concepts, tries, and union-find.

- `core_swe_dsa_tracker_2_algorithms.ipynb`  
  Split notebook focused on algorithms: complexity analysis, sorting, searching/binary search, recursion, backtracking, sliding window, two pointers, greedy algorithms, dynamic programming, graph traversal, shortest paths, topological sort, bit manipulation, and the problem log.

### Software Engineering Breadth

- `SWE_breadth_topics.ipynb`  
  Breadth notebook for software engineering concepts beyond DSA, including distributed systems and backend/system-design topics such as caching and consistent hashing.

## How to Use

Open the notebooks in Jupyter, VS Code, or another notebook editor. Use the checklists to track progress, run the examples, and add your own notes or practice solutions under each topic.

The split notebooks are the recommended files for day-to-day study because they are smaller and easier to navigate. The original full DSA tracker is kept for reference.

## Attribution

Author: `abpanick`

Created and refined with assistance from ChatGPT, Claude, and Perplexity.
