# Folder Reference

**Project:** Quantum Intelligence Lab (QIL)

**Purpose:** Define the responsibility, contents, and usage of every folder in the repository.

---

# Overview

QIL follows a modular architecture.

Each folder represents a subsystem with a single responsibility.

Folders should never overlap in functionality.

---

# Project Root

```
Quantum-Intelligence-Lab/
```

Purpose

Contains project-wide configuration, documentation, dependency management, and entry points.

Typical Contents

* README.md
* requirements.txt
* environment.yml
* run.py
* .gitignore

Should NOT Contain

* Model implementations
* Research modules
* Dataset processing logic

---

# app/

Purpose

Future application layer.

Responsibilities

* User interface
* Dashboard
* AI chat interface
* Interactive controls
* Visualization

Future Technologies

* Streamlit
* FastAPI
* React

Current Status

⬜ Planned

---

# configs/

Purpose

Centralized project configuration.

Current Files

* config.yaml

Responsibilities

* Dataset selection
* Random seeds
* Cross-validation settings
* Reporting options
* Model configuration

Rule

No module should hardcode configurable values.

---

# data/

Purpose

Dataset storage.

Contains

* CSV files
* Benchmark datasets
* Downloaded datasets
* Cached datasets

Should NOT Contain

* Reports
* Experiment logs
* Generated outputs

---

# experiments/

Purpose

Store experiment artifacts.

Future Contents

* Experiment snapshots
* Model checkpoints
* Serialized pipelines
* Metadata

Current Status

Reserved for future use.

---

# notebooks/

Purpose

Exploratory research.

Use Cases

* Early experimentation
* Data exploration
* Prototype ideas

Rule

Production code must eventually be moved into the `src/` package.

---

# reports/

Purpose

Store generated outputs.

Current Contents

* Benchmark CSV reports

Future Contents

* PDF reports
* HTML reports
* Publication reports
* Figures
* Charts

Rule

Nothing inside this folder should be manually edited.

---

# docs/

Purpose

Project documentation.

Contents

* Architecture
* Roadmap
* Progress
* Module reference
* AI context
* Coding standards

Audience

* Developers
* Researchers
* AI assistants

---

# src/

Purpose

Main source code.

All production code belongs here.

Submodules

* datasets
* preprocessing
* models
* evaluation
* reporting
* optimization
* explainability
* recommendations
* database
* benchmarking
* config
* utils

Rule

All importable project logic must reside under `src/`.

---

# src/datasets/

Purpose

Dataset Intelligence subsystem.

Responsibilities

* Load datasets
* Analyze datasets
* Compute dataset statistics
* Evaluate QML suitability

Current Components

* Dataset Loader
* Dataset Profiler
* Complexity Analyzer
* Correlation Analyzer
* Entropy Analyzer
* Class Balance Analyzer
* QML Suitability
* QRI Calculator
* Intelligence Engine

Input

Raw dataset.

Output

Dataset Intelligence Report.

---

# src/database/

Purpose

Experiment management.

Responsibilities

* Store experiments
* Read experiments
* Reproduce experiments
* Manage SQLite database

Current Components

* Database Manager
* Experiment Logger
* Experiment Reader
* Reproduction Engine

Output

Persistent research history.

---

# src/preprocessing/

Purpose

Research preprocessing pipeline.

Responsibilities

* Scaling
* Feature Selection
* PCA
* Future feature engineering

Current Components

* Scaler
* Feature Selector
* PCA Reducer
* Preprocessing Pipeline

Output

Processed dataset ready for benchmarking.

---

# src/models/

Purpose

Model implementations.

Structure

```
models/

classical/
quantum/
hybrid/
```

Goal

Keep model implementations isolated from benchmarking logic.

---

# src/models/classical/

Purpose

Classical machine learning models.

Current Models

* Logistic Regression
* Random Forest
* SVM
* XGBoost
* MLP

Additional Component

* Model Registry

Future Expansion

Additional classical algorithms.

---

# src/models/quantum/

Purpose

Quantum machine learning models.

Planned Models

* QSVM
* VQC
* EstimatorQNN
* SamplerQNN

Current Status

⬜ Planned

---

# src/models/hybrid/

Purpose

Hybrid classical-quantum models.

Planned Models

* Hybrid QNN
* Quantum Feature Extraction Pipelines
* Ensemble Architectures

Current Status

⬜ Planned

---

# src/evaluation/

Purpose

Evaluate model performance.

Current Components

* Train/Test Manager
* Metrics Calculator
* Cross Validator
* Statistical Analyzer

Responsibilities

* Model evaluation
* Metric computation
* Cross-validation
* Statistical summaries

---

# src/benchmarking/

Purpose

Coordinate benchmarking workflows.

Responsibilities

* Execute models
* Run evaluation pipelines
* Collect benchmark results
* Produce rankings

Current Component

* Classical Benchmark

Future Components

* Quantum Benchmark
* Hybrid Benchmark

---

# src/reporting/

Purpose

Generate research outputs.

Current Components

* Comparison Matrix

Future Components

* PDF Generator
* HTML Reports
* Publication Generator
* Visualization Utilities

---

# src/optimization/

Purpose

Hyperparameter optimization.

Planned Components

* Grid Search
* Random Search
* Bayesian Optimization

Current Status

⬜ Planned

---

# src/explainability/

Purpose

Model interpretability.

Planned Components

* Feature Importance
* Permutation Importance
* SHAP Integration
* Explainability Dashboard

Current Status

⬜ Planned

---

# src/recommendations/

Purpose

Research guidance.

Planned Responsibilities

* Model recommendations
* Dataset recommendations
* Optimization suggestions
* QML suitability recommendations

Current Status

⬜ Planned

---

# src/config/

Purpose

Configuration management.

Current Components

* Config Manager

Responsibilities

* Read configuration
* Validate configuration
* Expose project settings

---

# src/utils/

Purpose

Shared utilities.

Current Components

* Seed Manager

Future Components

* Logging utilities
* Common helper functions
* Timing utilities
* File utilities

Rule

Utilities must remain generic and reusable across modules.

---

# src/tests/

Purpose

Unit testing for source modules.

Current Tests

* Preprocessing
* Cross Validation

Future Tests

* Dataset Intelligence
* Database
* Benchmarking
* Quantum Models
* Explainability
* Optimization

Rule

Every major subsystem should have corresponding tests.

---

# tests/

Purpose

Repository-level integration and end-to-end testing.

Future Examples

* Full benchmark workflow
* End-to-end experiment execution
* Regression tests
* Performance tests

Current Status

Reserved for future use.

---

# Architectural Rules

Rule 1

Every folder must have a single responsibility.

Rule 2

Modules communicate through public interfaces, not internal implementation details.

Rule 3

Dependencies should always point downward.

Example

```
Application
    ↓
Reporting
    ↓
Evaluation
    ↓
Models
    ↓
Preprocessing
    ↓
Datasets
```

Lower layers must never import higher layers.

Rule 4

New functionality should extend existing modules rather than duplicating logic.

Rule 5

Every new subsystem should include:

* Documentation
* Unit tests
* Configuration support
* Integration with the overall architecture

---

# Folder Status Summary

| Folder               | Status      | Purpose                     |
| -------------------- | ----------- | --------------------------- |
| app                  | ⬜ Planned   | User interface              |
| configs              | ✅ Stable    | Project configuration       |
| data                 | ✅ Stable    | Dataset storage             |
| docs                 | ✅ Stable    | Documentation               |
| experiments          | 🟡 Reserved | Experiment artifacts        |
| notebooks            | ✅ Available | Research notebooks          |
| reports              | 🟡 Active   | Generated outputs           |
| src/datasets         | ✅ Complete  | Dataset Intelligence        |
| src/database         | ✅ Complete  | Experiment Tracking         |
| src/preprocessing    | ✅ Complete  | Data preprocessing          |
| src/models/classical | ✅ Complete  | Classical ML                |
| src/models/quantum   | ⬜ Planned   | Quantum ML                  |
| src/models/hybrid    | ⬜ Planned   | Hybrid ML                   |
| src/evaluation       | 🟡 Active   | Research evaluation         |
| src/benchmarking     | 🟡 Active   | Benchmark orchestration     |
| src/reporting        | 🟡 Active   | Research reporting          |
| src/optimization     | ⬜ Planned   | Hyperparameter optimization |
| src/explainability   | ⬜ Planned   | Explainable AI              |
| src/recommendations  | ⬜ Planned   | Research recommendations    |
| src/config           | ✅ Stable    | Configuration management    |
| src/utils            | 🟡 Growing  | Shared utilities            |
| src/tests            | 🟡 Growing  | Unit tests                  |
| tests                | ⬜ Planned   | Integration tests           |

---

# Summary

The folder organization of QIL reflects a layered, modular architecture designed for long-term maintainability and extensibility. Each subsystem has a clearly defined responsibility, allowing Classical Machine Learning, Quantum Machine Learning, Hybrid Intelligence, Explainability, Optimization, Reporting, and AI-assisted research capabilities to evolve independently while remaining part of a unified research platform.

---

**End of Document**
