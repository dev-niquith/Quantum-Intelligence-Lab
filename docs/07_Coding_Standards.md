# Coding Standards

**Project:** Quantum Intelligence Lab (QIL)

**Version:** 0.5.0 (Development)

---

# Purpose

This document defines the coding standards for Quantum Intelligence Lab (QIL).

The objectives are to:

* Maintain readability.
* Ensure consistency.
* Improve maintainability.
* Support collaborative development.
* Make the codebase understandable for both humans and AI assistants.

These standards apply to every module in the project.

---

# Core Engineering Principles

Every implementation should follow these principles.

## 1. Single Responsibility Principle (SRP)

Each class and module should have one clearly defined responsibility.

Good Example

```text
DatasetLoader

Loads datasets.
```

Bad Example

```text
DatasetLoader

Loads datasets
+
Trains models
+
Creates reports
```

---

## 2. Modular Design

Modules should remain independent.

Example

```text
datasets/

Only dataset-related logic.
```

Never place preprocessing, benchmarking or reporting logic inside the dataset module.

---

## 3. Reusability

Write components that can be reused by:

* Classical ML
* Quantum ML
* Hybrid ML

Avoid implementations tied to a single model unless absolutely necessary.

---

## 4. Extensibility

Every design decision should make adding future functionality easier.

Example

A new model such as QSVM should be added without modifying the Benchmark Runner.

---

# Python Style

Follow the recommendations of **PEP 8** unless there is a project-specific reason to do otherwise.

Guidelines

* Four spaces for indentation.
* Maximum line length around 88-100 characters.
* One import per line.
* Blank lines between logical sections.

---

# Naming Conventions

## Files

Use lowercase with underscores.

Examples

```text
dataset_loader.py
metrics_calculator.py
cross_validator.py
```

Avoid

```text
DatasetLoader.py
Metrics.py
MyFile.py
```

---

## Classes

Use PascalCase.

Examples

```text
DatasetLoader
CrossValidator
StatisticalAnalyzer
ModelRegistry
```

---

## Functions

Use snake_case.

Examples

```python
load_dataset()
calculate_metrics()
run_benchmark()
save_experiment()
```

---

## Variables

Use descriptive names.

Good

```python
feature_matrix
target_labels
experiment_results
confidence_interval
```

Avoid

```python
a
b
temp
data1
```

---

## Constants

Use uppercase.

Example

```python
DEFAULT_RANDOM_SEED = 42
MAX_ITERATIONS = 1000
```

---

# Imports

Always use absolute imports.

Preferred

```python
from src.datasets.dataset_loader import DatasetLoader
```

Avoid

```python
from datasets.dataset_loader import DatasetLoader
```

Avoid wildcard imports.

Incorrect

```python
from module import *
```

---

# File Structure

A typical module should follow this order.

```text
Module Docstring

Imports

Constants

Class Definitions

Helper Functions

Main Execution (if required)
```

---

# Docstrings

Every public class and function should include a docstring.

Class Example

```python
class DatasetLoader:
    """
    Load datasets supported by QIL.

    Responsibilities
    ----------------
    - Load benchmark datasets.
    - Return features and labels.
    """
```

Function Example

```python
def load_dataset(name):
    """
    Load a dataset by name.

    Parameters
    ----------
    name : str

    Returns
    -------
    X
    y
    """
```

---

# Comments

Comments should explain intent.

Good

```python
# Standardize feature values before PCA.
```

Avoid

```python
# Increment i
i += 1
```

The code already explains that.

---

# Error Handling

Handle expected errors gracefully.

Preferred

```python
try:
    ...
except FileNotFoundError:
    ...
```

Avoid broad exception handling.

Incorrect

```python
except:
    ...
```

Catch specific exceptions whenever possible.

---

# Configuration

Project settings belong in:

```text
configs/config.yaml
```

Avoid hardcoded values.

Good

```python
random_seed = config["random_seed"]
```

Avoid

```python
random_seed = 42
```

unless it is a documented default.

---

# Logging

Prefer structured logging over excessive print statements.

Development

```python
print("Benchmark started.")
```

Future

```python
logger.info("Benchmark started.")
```

Logging will gradually replace debugging prints as QIL matures.

---

# Type Hints

Use type hints where they improve readability.

Example

```python
def load_dataset(name: str):
```

Example

```python
def calculate_metrics(
    y_true,
    y_pred
) -> dict:
```

---

# Testing

Every major subsystem should include unit tests.

Suggested naming

```text
test_dataset_loader.py
test_cross_validator.py
test_model_registry.py
```

Tests should verify:

* Correct outputs.
* Edge cases.
* Invalid inputs.
* Reproducibility where applicable.

---

# Module Boundaries

Each module owns a specific responsibility.

| Module          | Responsibility          |
| --------------- | ----------------------- |
| datasets        | Dataset analysis        |
| preprocessing   | Data preparation        |
| models          | Model implementations   |
| evaluation      | Metric computation      |
| benchmarking    | Benchmark orchestration |
| reporting       | Report generation       |
| explainability  | Model interpretation    |
| optimization    | Hyperparameter tuning   |
| recommendations | Research guidance       |

Do not mix responsibilities across modules.

---

# Architectural Dependency Rules

Dependencies should always flow downward.

Correct

```text
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

Incorrect

```text
Datasets
    ↓
Reporting
```

Lower layers must never depend on higher layers.

---

# Benchmark Standards

Every benchmark should include:

* Preprocessing
* Cross Validation
* Multiple evaluation metrics
* Statistical summaries
* Reproducible configuration

Benchmarks should not rely on a single train/test split.

---

# Documentation Standards

Every completed subsystem should include:

* Docstrings
* Unit tests
* Documentation updates
* Integration notes

Major architectural changes should also update:

* `01_System_Architecture.md`
* `02_Current_Progress.md`
* `03_Development_Roadmap.md`
* `05_Module_Reference.md`
* `06_AI_CONTEXT.md`

---

# Git Workflow

Each completed milestone should follow this sequence.

1. Run tests.
2. Review code.
3. Update documentation.
4. Commit changes.
5. Push to GitHub.
6. Create a version tag for stable milestones.

Commit messages should be clear.

Good

```text
Implemented cross validation engine
```

Good

```text
Added SHAP explainability module
```

Avoid

```text
Update
```

```text
Fix
```

```text
Changes
```

---

# AI Collaboration Guidelines

When using AI assistants during development:

* Preserve existing architecture.
* Avoid introducing duplicate functionality.
* Prefer extending existing modules over creating new ones.
* Explain architectural changes before implementing them.
* Keep generated code consistent with project conventions.
* Ensure new code remains compatible with future Classical, Quantum and Hybrid integrations.

---

# Definition of Done

A feature is considered complete only when:

* Implementation is finished.
* Code follows project standards.
* Unit tests pass.
* Documentation is updated.
* Integration is verified.
* Changes are committed and pushed.
* A stable version tag is created when appropriate.

---

# Final Principle

Every contribution to QIL should improve at least one of the following:

* Readability
* Maintainability
* Extensibility
* Reproducibility
* Research quality
* Software architecture
* User experience

The goal is not simply to write code, but to build a research-grade engineering platform that remains understandable and extensible as it grows.

---

**End of Document**
