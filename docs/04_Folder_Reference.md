# Folder Reference

**Project:** Quantum Intelligence Lab (QIL)

**Version:** v1.0.0

---

# Purpose

This document defines the responsibility, contents, and intended usage of every folder within the Quantum Intelligence Lab (QIL) repository.

Unlike the Module Reference, which describes software components, this document focuses on the physical organization of the project.

Every folder in QIL has a clearly defined responsibility and should avoid overlapping functionality.

This organization supports:

* Maintainability
* Modularity
* Reproducibility
* Scalability
* Collaboration

---

# Repository Overview

QIL follows a layered and modular architecture.

Each directory represents a subsystem within the overall research platform.

The repository is organized so that documentation, datasets, experiments, reports, configuration, and source code evolve independently while remaining fully integrated.

Current high-level structure:

```text
Quantum-Intelligence-Lab/
│
├── configs/
├── data/
├── docs/
├── experiments/
├── notebooks/
├── reports/
├── src/
├── tests/
│
├── run.py
├── requirements.txt
├── environment.yml
└── README.md
```

---

# Project Root

```text
Quantum-Intelligence-Lab/
```

Purpose

Contains project-wide resources and serves as the entry point for the entire platform.

Typical Contents

* README.md
* requirements.txt
* environment.yml
* run.py
* .gitignore

Responsibilities

* Dependency management
* Project initialization
* Environment setup
* Repository metadata

Should NOT Contain

* Model implementations
* Benchmark logic
* Dataset processing
* Evaluation code

---

# app/

Purpose

Future application layer.

Responsibilities

* Interactive user interface
* Dashboard
* AI Research Copilot interface
* Dataset upload
* Experiment configuration
* Interactive visualizations

Potential Technologies

* Streamlit
* FastAPI
* React

Current Status

⬜ Planned

---

# configs/

Purpose

Centralized configuration management.

Current Files

* config.yaml

Responsibilities

* Dataset selection
* Random seed configuration
* Cross-validation settings
* Model parameters
* Reporting options
* Benchmark settings

Design Principle

Configuration values should never be hardcoded inside application modules.

Current Status

✅ Stable

---

# data/

Purpose

Central storage for datasets used throughout QIL.

Contains

* Benchmark datasets
* CSV files
* Downloaded datasets
* Cached datasets

Future Contents

* OpenML datasets
* Custom research datasets
* Domain-specific datasets
* Synthetic datasets

Should NOT Contain

* Reports
* Logs
* Generated outputs

Current Status

✅ Stable

---

# experiments/

Purpose

Persistent storage for experiment artifacts.

Future Contents

* Experiment snapshots
* Serialized preprocessing pipelines
* Model checkpoints
* Metadata
* Configuration snapshots
* Experiment history

Design Goal

Every experiment should be reproducible using only the contents stored in this directory.

Current Status

🟡 Reserved for Future Expansion

---

# notebooks/

Purpose

Interactive research and rapid prototyping.

Typical Use Cases

* Exploratory Data Analysis (EDA)
* Prototype development
* Algorithm validation
* Visualization experiments

Engineering Rule

Any notebook code that becomes production-ready should be migrated into the `src/` package.

Current Status

✅ Available

---

# reports/

Purpose

Store all automatically generated research outputs.

Current Contents

* Timestamped benchmark CSV reports
* Research benchmark summaries

Example Outputs

```text
breast_cancer_20260707_001221.csv
iris_20260707_153812.csv
wine_20260708_094516.csv
```

Future Contents

* PDF reports
* HTML reports
* Publication-ready reports
* Visualizations
* Figures
* Statistical summaries

Design Principle

Reports are generated automatically and should never require manual editing.

Current Status

✅ Stable

---

# docs/

Purpose

Central repository for all project documentation.

Current Documents

* Project Overview
* System Architecture
* Current Progress
* Development Roadmap
* Folder Reference
* Module Reference
* AI Context
* Coding Standards
* Research Methodology
* Development Log
* Future Vision

Audience

* Developers
* Researchers
* Contributors
* AI Assistants

Current Status

✅ Stable

---

# src/

Purpose

Primary source code for Quantum Intelligence Lab.

All production-ready implementation belongs inside this package.

Current Submodules

* datasets
* preprocessing
* models
* evaluation
* benchmarking
* reporting
* database
* config
* utils

Future Submodules

* optimization
* explainability
* recommendations
* copilot

Engineering Rule

Every importable module should reside under `src/`.

Current Status

✅ Stable

---

# src/datasets/

Purpose

Dataset Intelligence subsystem.

Responsibilities

* Load benchmark datasets
* Profile datasets
* Compute descriptive statistics
* Analyze feature relationships
* Estimate dataset complexity
* Evaluate Quantum Machine Learning suitability
* Calculate the Quantum Readiness Index (QRI)

Current Components

* DatasetLoader
* DatasetProfiler
* ComplexityAnalyzer
* CorrelationAnalyzer
* EntropyAnalyzer
* ClassBalanceAnalyzer
* QMLSuitabilityAnalyzer
* QRICalculator
* IntelligenceEngine

Inputs

* Dataset name
* Raw feature matrix
* Target labels

Outputs

* Dataset Intelligence Report
* QRI Score
* QML Suitability Score
* Dataset statistics

Current Status

✅ Complete

---

# src/database/

Purpose

Manage experiment tracking and reproducibility.

Responsibilities

* Store experiment metadata
* Retrieve experiment history
* Restore previous experiments
* Maintain SQLite database

Current Components

* DatabaseManager
* ExperimentLogger
* ExperimentReader
* ReproductionEngine

Outputs

* Persistent experiment records
* Experiment metadata
* Reproducible configurations

Current Status

✅ Complete

---

# src/preprocessing/

Purpose

Provide a unified preprocessing pipeline for all benchmarking workflows.

Responsibilities

* Feature scaling
* Feature selection
* PCA dimensionality reduction
* Consistent preprocessing

Current Components

* Scaler
* FeatureSelector
* PCAReducer
* PreprocessingPipeline

Outputs

* Research-ready processed datasets

Engineering Principle

Every model should receive identical preprocessing to ensure fair comparisons.

Current Status

✅ Complete

---

# src/models/

Purpose

Contain every machine learning model implemented within QIL.

Structure

```text
models/
│
├── classical/
├── quantum/
└── hybrid/
```

Design Goal

Separate model implementation from evaluation and benchmarking logic.

Current Status

🟡 Growing

---

# src/models/classical/

Purpose

Implement Classical Machine Learning algorithms.

Current Models

* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)
* XGBoost
* Multi-Layer Perceptron (MLP)

Supporting Components

* ModelRegistry

Responsibilities

* Standardized interfaces
* Model registration
* Training
* Prediction

Current Status

✅ Complete

Future Expansion

* LightGBM
* CatBoost
* Extra Trees
* AdaBoost

---

# src/models/quantum/

Purpose

Implement native Quantum Machine Learning models.

Planned Models

* QSVM
* Variational Quantum Classifier (VQC)
* EstimatorQNN
* SamplerQNN

Dependencies

* Qiskit
* Qiskit Machine Learning
* PennyLane

Future Responsibilities

* Quantum kernels
* Feature maps
* Variational circuits
* Hardware execution

Current Status

⬜ Planned

---

# src/models/hybrid/

Purpose

Combine Classical and Quantum learning techniques.

Planned Models

* Hybrid Quantum Neural Networks
* Quantum Feature Extraction Pipelines
* Ensemble Architectures

Future Responsibilities

* Hybrid training workflows
* Shared optimization
* Integrated evaluation

Current Status

⬜ Planned

---

# src/evaluation/

Purpose

Provide research-grade model evaluation.

Responsibilities

* Cross-validation
* Metric computation
* Statistical analysis
* Performance aggregation

Current Components

* TrainTestManager
* MetricsCalculator
* CrossValidator
* StatisticalAnalyzer

Current Features

* Stratified K-Fold Cross Validation
* Accuracy
* Precision
* Recall
* F1 Score
* Mean
* Median
* Minimum
* Maximum
* Standard Deviation
* 95% Confidence Interval

Engineering Goal

Evaluate model reliability rather than relying on a single train/test split.

Current Status

✅ Complete

Future Enhancements

* Nested Cross Validation
* Bootstrap Evaluation
* Parallel Cross Validation

---

# src/benchmarking/

Purpose

Coordinate benchmarking across all supported learning paradigms.

Responsibilities

* Execute registered models
* Apply unified preprocessing
* Run cross-validation
* Aggregate statistics
* Rank models
* Generate leaderboard

Current Components

* ResearchBenchmark

Future Components

* QuantumBenchmark
* HybridBenchmark

Current Features

* Unified benchmarking workflow
* Automatic model ranking
* Statistical comparison
* Integrated report generation

Current Status

✅ Complete

---

# src/reporting/

Purpose

Generate research outputs and benchmark reports.

Responsibilities

* Build comparison matrices
* Export benchmark results
* Generate research summaries
* Save benchmark outputs

Current Components

* ComparisonMatrix

Current Features

* Timestamped CSV generation
* Dataset-aware filenames
* Research benchmark summaries

Example Output

```text
reports/

breast_cancer_20260707_001221.csv
iris_20260708_154533.csv
```

Future Components

* PDF Generator
* HTML Reports
* Publication Generator
* Visualization Utilities

Current Status

✅ Complete

---


# src/optimization/

Purpose

Automatically discover optimal model configurations.

Planned Components

* Grid Search
* Random Search
* Bayesian Optimization
* Hyperparameter Search Engine

Expected Outputs

* Best parameter configuration
* Optimization reports
* Performance comparison

Current Status

⬜ Planned

---

# src/explainability/

Purpose

Interpret and explain model predictions.

Planned Components

* Feature Importance
* Permutation Importance
* SHAP Integration
* Explainability Dashboard

Expected Outputs

* Feature rankings
* Global explanations
* Local explanations
* Visualization reports

Current Status

⬜ Planned

---

# src/recommendations/

Purpose

Generate intelligent research recommendations.

Planned Responsibilities

* Model recommendations
* Dataset recommendations
* Hyperparameter suggestions
* QML suitability guidance
* Research insights

Expected Outputs

* Recommendation reports
* Decision-support summaries

Current Status

⬜ Planned

---

# src/copilot/

Purpose

Serve as the AI Research Copilot for QIL.

Future Responsibilities

* Explain benchmark results
* Interpret statistical analysis
* Compare models
* Recommend experiments
* Answer QML questions
* Generate publication drafts
* Retrieve experiment history

Potential Technologies

* Local LLMs
* Retrieval-Augmented Generation (RAG)
* Vector Database
* Tool Calling
* Research Memory

Current Status

⬜ Planned

---

# src/config/

Purpose

Centralized configuration management.

Current Components

* ConfigManager

Responsibilities

* Load YAML configuration
* Reload configuration
* Nested configuration access
* Runtime configuration sharing

Current Features

* Dot-notation access
* Single configuration source
* Shared configuration across modules

Future Enhancements

* Configuration validation
* Environment profiles
* Runtime overrides
* CLI configuration

Current Status

✅ Stable

---

# src/utils/

Purpose

Provide reusable utilities shared across the platform.

Current Components

* SeedManager

Responsibilities

* Random seed management
* Shared helper utilities
* Common project functions

Future Components

* Logging utilities
* Timing utilities
* File utilities
* Serialization helpers

Engineering Principle

Utility modules should remain generic and independent of higher-level business logic.

Current Status

🟡 Growing

---

# src/tests/

Purpose

Provide unit testing for individual source modules.

Current Coverage

* Preprocessing Pipeline
* Cross Validation
* Statistical Evaluation
* Benchmark Integration

Future Coverage

* Dataset Intelligence
* Database
* Reporting
* Quantum Models
* Explainability
* Optimization
* AI Copilot

Engineering Goal

Every production module should have corresponding automated tests.

Current Status

🟡 Growing

---

# tests/

Purpose

Repository-level integration and end-to-end testing.

Future Examples

* Complete benchmark workflow
* Full experiment lifecycle
* Multi-dataset execution
* Performance regression tests
* System integration tests

Current Status

⬜ Planned

---

# Architectural Rules

Rule 1

Every folder must have a single, clearly defined responsibility.

---

Rule 2

Modules communicate only through stable public interfaces.

Internal implementation details should remain encapsulated.

---

Rule 3

Dependencies always flow downward through the architecture.

```text
Application
        ↓
AI Copilot
        ↓
Reporting
        ↓
Benchmarking
        ↓
Evaluation
        ↓
Models
        ↓
Preprocessing
        ↓
Dataset Intelligence
        ↓
Configuration / Utilities
```

Lower architectural layers must never depend on higher layers.

---

Rule 4

New functionality should extend existing modules rather than duplicate implementation.

---

Rule 5

Every major subsystem should include:

* Documentation
* Configuration support
* Unit tests
* Integration into the research workflow

---

Rule 6

Generated artifacts (reports, experiment records, future model checkpoints) should always be uniquely identifiable using dataset-aware and timestamp-based naming conventions.

---

# Folder Status Summary

| Folder | Status | Purpose |
|----------|---------|------------------------------|
| app | ⬜ Planned | User Interface |
| configs | ✅ Stable | Project Configuration |
| data | ✅ Stable | Dataset Storage |
| docs | ✅ Stable | Documentation |
| experiments | 🟡 Reserved | Experiment Artifacts |
| notebooks | ✅ Available | Research & Prototyping |
| reports | ✅ Stable | Generated Research Reports |
| src/datasets | ✅ Complete | Dataset Intelligence |
| src/database | ✅ Complete | Experiment Tracking |
| src/preprocessing | ✅ Complete | Research Preprocessing |
| src/models/classical | ✅ Complete | Classical ML Models |
| src/models/quantum | ⬜ Planned | Quantum ML Models |
| src/models/hybrid | ⬜ Planned | Hybrid ML Models |
| src/evaluation | ✅ Complete | Research Evaluation |
| src/benchmarking | ✅ Complete | Benchmark Orchestration |
| src/reporting | ✅ Complete | Research Reporting |
| src/optimization | ⬜ Planned | Hyperparameter Optimization |
| src/explainability | ⬜ Planned | Explainable AI |
| src/recommendations | ⬜ Planned | Research Recommendations |
| src/copilot | ⬜ Planned | AI Research Copilot |
| src/config | ✅ Stable | Configuration Management |
| src/utils | 🟡 Growing | Shared Utilities |
| src/tests | 🟡 Growing | Unit Testing |
| tests | ⬜ Planned | Integration Testing |

---

# Summary

The folder organization of Quantum Intelligence Lab (QIL) reflects a layered, modular architecture designed for long-term maintainability, reproducibility, and extensibility. Each directory has a clearly defined responsibility and communicates through stable interfaces, enabling Classical Machine Learning, Quantum Machine Learning, Hybrid Intelligence, Explainability, Optimization, Reporting, and AI-assisted research capabilities to evolve independently while remaining part of a unified research platform.

Following the completion of **QIL v1.0**, the repository now provides a fully operational classical research benchmarking pipeline featuring dataset intelligence, reproducible experimentation, unified preprocessing, statistical evaluation, automated benchmarking, comparison reporting, and timestamped research report generation. Future development will build upon this stable foundation by introducing Quantum ML, Hybrid ML, Explainability, Optimization, and the AI Research Copilot.

---

**End of Document**