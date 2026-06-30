# AI_CONTEXT.md

**Project:** Quantum Intelligence Lab (QIL)

**Purpose:** AI Project Context File

**Audience:** Large Language Models (LLMs), AI Coding Assistants, Future Contributors

---

# Project Summary

Quantum Intelligence Lab (QIL) is a modular, research-grade Quantum Machine Learning platform.

The project is designed to bridge the gap between Classical Machine Learning and Quantum Machine Learning by providing a unified framework for:

* Dataset Intelligence
* Experiment Tracking
* Research Evaluation
* Explainability
* Classical Benchmarking
* Quantum Benchmarking
* Hybrid ML Benchmarking
* Research Recommendations
* AI-Assisted Research

QIL is **not** a notebook collection or algorithm demo. It is engineered as extensible software.

---

# Primary Objective

Build a production-quality research platform that demonstrates:

* Software Engineering
* Machine Learning Engineering
* Quantum Machine Learning Engineering
* Research Methodology
* Explainable AI
* Product Development

The project is intended to be portfolio-quality and showcase engineering ability rather than isolated model performance.

---

# Development Philosophy

Every implementation must satisfy these principles:

1. Single Responsibility Principle.
2. Modular architecture.
3. Reusable interfaces.
4. Research-first engineering.
5. Extensibility for future Quantum ML models.
6. Readable, well-commented code.
7. Reproducible experiments.
8. Production-style project organization.

---

# Technology Stack

Programming Language

* Python 3.11+

Core Libraries

* NumPy
* pandas
* scikit-learn
* XGBoost

Quantum Libraries (Planned)

* Qiskit
* Qiskit Machine Learning
* PennyLane (Future)

Visualization (Planned)

* Matplotlib
* Plotly

Database

* SQLite

Configuration

* YAML

Future AI Stack

* LangChain or LlamaIndex
* Local LLM support
* Vector Database
* Retrieval-Augmented Generation (RAG)

---

# Current Repository Structure

```text id="j3sryg"
configs/
data/
docs/
experiments/
notebooks/
reports/

src/
    benchmarking/
    config/
    database/
    datasets/
    evaluation/
    explainability/
    models/
        classical/
        quantum/
        hybrid/
    optimization/
    preprocessing/
    recommendations/
    reporting/
    tests/
    utils/

run.py
```

---

# Completed Modules

Dataset Intelligence

Status

✅ Complete

Components

* Dataset Loader
* Dataset Profiler
* Complexity Analyzer
* Correlation Analyzer
* Entropy Analyzer
* Class Balance Analyzer
* QML Suitability
* Quantum Readiness Index (QRI)

---

Experiment Tracking

Status

✅ Complete

Components

* Database Manager
* Experiment Logger
* Experiment Reader
* Reproduction Engine
* Configuration Manager

---

Research Preprocessing

Status

✅ Complete

Components

* Standard Scaler
* Feature Selector
* PCA Reducer
* Unified Preprocessing Pipeline

---

Classical Machine Learning

Status

✅ Complete

Models

* Logistic Regression
* Random Forest
* SVM
* XGBoost
* MLP

---

Evaluation

Status

🟡 Active Development

Completed

* Metrics Calculator
* Stratified Cross Validation
* Statistical Analyzer

In Progress

* Benchmark Integration

---

Reporting

Status

🟡 Active Development

Completed

* Comparison Matrix
* CSV Export

---

# Planned Modules

Optimization

* Grid Search
* Random Search
* Bayesian Optimization

Explainability

* Feature Importance
* Permutation Importance
* SHAP

Quantum ML

* QSVM
* VQC
* EstimatorQNN
* SamplerQNN

Hybrid ML

* Hybrid Quantum Neural Networks

Research Intelligence

* Recommendation Engine
* Stability Analysis
* Resource Analysis

AI Layer

* AI Research Copilot
* Research Memory
* Natural Language Query System

Application

* Streamlit Dashboard
* FastAPI Backend
* React Frontend (Future)

---

# Current Data Flow

```text id="xej92i"
Dataset
    ↓
Dataset Intelligence
    ↓
Experiment Tracking
    ↓
Preprocessing
    ↓
Model Registry
    ↓
Benchmark Runner
    ↓
Cross Validation
    ↓
Metrics Calculator
    ↓
Statistical Analyzer
    ↓
Comparison Matrix
    ↓
Reports
```

Future flow extends this pipeline with Explainability, Quantum Models, Recommendation Engine and AI Research Copilot.

---

# Coding Standards

Always follow these conventions.

Imports

* Absolute imports using `src.` prefix.
* Avoid relative imports unless necessary.

Classes

* One primary responsibility per class.
* Descriptive class names.

Functions

* Small and reusable.
* Include docstrings.
* Avoid duplicated logic.

Comments

* Explain intent, not obvious syntax.
* Keep comments concise and meaningful.

Variables

* Use descriptive names.
* Avoid unnecessary abbreviations.

Configuration

* Read configurable values from `config.yaml` whenever appropriate.
* Do not hardcode values that may change between experiments.

---

# Architectural Rules

Never violate these constraints.

1. Lower layers must never import higher layers.

Correct

```text id="h3zt0w"
Reporting
    ↓
Evaluation
    ↓
Models
```

Incorrect

```text id="jlwmgc"
Models
    ↓
Reporting
```

2. Benchmarking should not implement models.

3. Models should not compute statistics.

4. Reporting should not train models.

5. Dataset Intelligence should not perform benchmarking.

6. Every subsystem must have a single responsibility.

---

# Development Workflow

Every new feature should follow this order:

1. Design the module.
2. Create folder structure if required.
3. Implement functionality.
4. Add docstrings and comments.
5. Write unit tests.
6. Integrate into the pipeline.
7. Update documentation.
8. Commit changes.
9. Tag stable versions.

---

# Current Sprint

Sprint 5

Objective

Complete the Research Evaluation Engine.

Remaining Tasks

* Integrate Cross Validator into Benchmark Runner.
* Upgrade benchmark reporting.
* Improve statistical summaries.
* Complete integration tests.

---

# Immediate Next Sprint

Sprint 6

Focus

Hyperparameter Optimization

Planned Components

* Grid Search
* Random Search
* Optimization Reports
* Automatic Best Model Selection

---

# Long-Term Vision

Version 1.0 should provide:

* Dataset Intelligence
* Experiment Tracking
* Classical Benchmarking
* Quantum Benchmarking
* Hybrid Benchmarking
* Explainability
* Hyperparameter Optimization
* Quantum Resource Analysis
* Research Recommendations
* Publication Report Generation
* AI Research Copilot
* Interactive Web Application

---

# AI Assistant Guidelines

If you are assisting with this project:

1. Preserve the modular architecture.
2. Prefer reusable solutions over shortcuts.
3. Maintain backward compatibility.
4. Keep implementations beginner-friendly but professionally structured.
5. Suggest improvements only if they align with the existing architecture.
6. Avoid introducing unnecessary complexity.
7. Always consider future Classical, Quantum and Hybrid model integration.

---

# Success Criteria

The project should ultimately be recognized as a research-grade engineering platform rather than a traditional machine learning repository.

A successful contribution should improve one or more of the following:

* Maintainability
* Extensibility
* Reproducibility
* Explainability
* Statistical validity
* Software architecture
* Research usability

---

# End of AI Context

This file is intended to be uploaded to AI assistants at the beginning of future development sessions. It provides sufficient architectural, technical and project context for productive collaboration without requiring the entire repository to be analyzed first.
