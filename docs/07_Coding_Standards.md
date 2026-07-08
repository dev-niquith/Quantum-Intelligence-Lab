# Coding Standards

**Project:** Quantum Intelligence Lab (QIL)

**Version:** v1.0.0 (Classical Research Platform)

---

# Purpose

This document defines the coding standards for Quantum Intelligence Lab (QIL).

The objectives are to:

* Maintain readability.
* Ensure consistency.
* Improve maintainability.
* Support collaborative development.
* Preserve reproducibility.
* Make the codebase understandable for both developers and AI assistants.

These standards apply to every module within QIL.

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
Runs benchmarks
+
Generates reports
```

Every class should solve exactly one problem.

---

## 2. Modular Design

Modules should remain independent.

Example

```text
datasets/

Only dataset-related logic.
```

Never place preprocessing, benchmarking or reporting logic inside dataset modules.

---

## 3. Reusability

Write components that can be reused by:

* Classical ML
* Quantum ML
* Hybrid ML

Avoid implementations tied to a single algorithm whenever possible.

---

## 4. Extensibility

Design new functionality so future features require minimal modification.

Example

A new model such as QSVM should be registered through the Model Registry without modifying the benchmark engine.

---

## 5. Research-First Engineering

QIL is a research platform.

Engineering decisions should prioritize:

* Reproducibility
* Statistical validity
* Fair benchmarking
* Maintainability

rather than only execution speed.

---

# Python Style

Follow **PEP 8** unless a documented project-specific exception exists.

Guidelines

* Four-space indentation
* Line length around 88–100 characters
* One import per line
* Blank lines between logical sections
* Meaningful whitespace for readability

---

# Naming Conventions

## Files

Use lowercase with underscores.

Examples

```text
dataset_loader.py
cross_validator.py
research_benchmark.py
config_manager.py
```

Avoid

```text
DatasetLoader.py
Benchmark.py
Utility.py
```

---

## Classes

Use PascalCase.

Examples

```text
DatasetLoader
CrossValidator
StatisticalAnalyzer
ResearchBenchmark
ConfigManager
```

---

## Functions

Use snake_case.

Examples

```python
load_dataset()
calculate_metrics()
execute_benchmark()
save_results()
```

---

## Variables

Use descriptive names.

Good

```python
feature_matrix
target_labels
benchmark_results
confidence_interval
dataset_name
output_directory
```

Avoid

```python
a
temp
value
data1
```

---

## Constants

Use uppercase.

Example

```python
DEFAULT_RANDOM_SEED = 42
REPORT_DIRECTORY = "reports"
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

Never use wildcard imports.

Incorrect

```python
from module import *
```

Prefer explicit imports for readability.



# File Structure

Every module should follow this order.

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

Every public class and function should include a complete docstring.

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

Docstrings should describe purpose rather than implementation.

---

# Comments

Comments should explain intent.

Good

```python
# Standardize features before PCA.
```

Avoid

```python
# Increment i
i += 1
```

The code should explain obvious operations.

---

# Error Handling

Handle expected errors explicitly.

Preferred

```python
try:
    ...
except FileNotFoundError:
    ...
```

Avoid

```python
except:
    ...
```

Catch only the exceptions you expect.

---

# Configuration

All configurable values belong in

```text
configs/config.yaml
```

Preferred

```python
random_seed = config.get("random_seed")
```

Avoid

```python
random_seed = 42
```

unless it is a documented fallback value.

---

# Reporting Standards

Generated reports should:

* Include dataset-aware filenames
* Include timestamps
* Never overwrite previous reports
* Preserve experiment history

Preferred filenames

```text
breast_cancer_20260707_001221.csv

iris_20260708_143012.csv

wine_20260709_103540.csv
```

Avoid generic filenames such as

```text
results.csv

benchmark.csv
```

---

# Logging

Prefer structured logging over print statements.

Current

```python
print("Benchmark started.")
```

Future

```python
logger.info("Benchmark started.")
```

---

# Type Hints

Use type hints whenever they improve readability.

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

Suggested names

```text
test_dataset_loader.py

test_cross_validator.py

test_research_benchmark.py
```

Tests should verify

* Correct outputs
* Invalid inputs
* Edge cases
* Reproducibility
* Configuration loading

---

# Module Boundaries

Each module owns one responsibility.

| Module | Responsibility |
|----------|----------------|
| datasets | Dataset analysis |
| preprocessing | Data preparation |
| models | Model implementation |
| evaluation | Metrics & statistics |
| benchmarking | Benchmark orchestration |
| reporting | Report generation |
| explainability | Model interpretation |
| optimization | Hyperparameter tuning |
| recommendations | Research guidance |

Responsibilities should never overlap.

---

# Architectural Dependency Rules

Dependencies always flow downward.

Correct

```text
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
Datasets
```

Incorrect

```text
Datasets
    ↓
Reporting
```

Lower layers must never depend on higher layers.



# Benchmark Standards

Every benchmark should include:

* Unified preprocessing
* Stratified Cross Validation
* Multiple evaluation metrics
* Statistical summaries
* Dataset-aware reporting
* Reproducible configuration

Benchmarks should never rely solely on a single train/test split.

---

# Documentation Standards

Every completed subsystem must include:

* Docstrings
* Unit tests
* Documentation updates
* Integration verification

Whenever architecture changes, update:

* `00_Project_Overview.md`
* `01_System_Architecture.md`
* `02_Current_Progress.md`
* `03_Development_Roadmap.md`
* `04_Folder_Reference.md`
* `05_Module_Reference.md`
* `06_AI_CONTEXT.md`
* `08_Research_Methodology.md`
* `09_Development_Log.md`
* `10_Future_Vision.md`

Documentation is treated as part of the implementation rather than an afterthought.

---

# Git Workflow

Every completed milestone should follow this sequence.

1. Run unit tests.
2. Verify benchmark outputs.
3. Review code.
4. Update documentation.
5. Commit changes.
6. Push to GitHub.
7. Create a stable version tag.

Good commit messages

```text
Implemented Research Benchmark Engine

Added timestamped dataset-aware reporting

Completed Statistical Evaluation Engine
```

Avoid

```text
Update

Fix

Changes
```

---

# AI Collaboration Guidelines

When using AI assistants during development:

* Preserve modular architecture.
* Extend existing modules before creating new ones.
* Avoid duplicate functionality.
* Respect established interfaces.
* Keep implementations beginner-friendly yet professionally structured.
* Explain architectural changes before implementation.
* Update documentation whenever functionality changes.
* Consider future Classical, Quantum and Hybrid compatibility.

AI-generated code should integrate naturally with the existing architecture instead of introducing isolated solutions.

---

# Definition of Done

A feature is complete only when:

* Implementation is finished.
* Coding standards are satisfied.
* Unit tests pass.
* Integration is verified.
* Documentation is updated.
* Reports generate correctly.
* Changes are committed and pushed.
* Stable version tags are created when appropriate.

---

# Final Principle

Every contribution to Quantum Intelligence Lab should improve at least one of the following:

* Readability
* Maintainability
* Extensibility
* Reproducibility
* Statistical validity
* Research quality
* Software architecture
* Documentation quality
* User experience

The objective is not merely to write working code, but to build a long-term, research-grade Machine Learning and Quantum Machine Learning engineering platform that remains understandable, reproducible and extensible as it evolves.

---

**End of Document**

