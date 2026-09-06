# Self-Prep

Study and interview-prep notebooks for machine learning, software engineering fundamentals, data structures, algorithms, and system-design breadth.

## Contents

### ML: Zero to Hero (in progress)

A course in notebook form, in **[`ML-Zero-to-Hero/`](ML-Zero-to-Hero/)**. Each notebook takes
one topic from "I have never fitted a model" to "I can build it, break it, diagnose it and
defend it in an interview" — theory built from scratch, a full worked example, hard questions,
practice datasets, and the research papers behind each section.

**Start with [`ML-Zero-to-Hero/README.md`](ML-Zero-to-Hero/README.md)** for the reading order.

Complete so far: **Foundations → Linear Regression → Logistic Regression → Decision Trees →
Random Forest → Gradient Boosting → SVMs → KNN → Naive Bayes → PCA** (10 of 16).

Every completed notebook has had all of its code cells executed in order with warnings treated
as errors, and every number quoted in its prose checked against what the code actually printed.
Where a result contradicted the point being made, the prose was rewritten to match the result —
those cases are flagged in the notebooks and are usually the most useful parts.

- [`ML-Zero-to-Hero/`](ML-Zero-to-Hero/) — the notebooks and the reader's guide
- [`ZERO_TO_HERO_PLAN.md`](ZERO_TO_HERO_PLAN.md) — the build plan, quality bar, per-notebook
  briefs and status log
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
