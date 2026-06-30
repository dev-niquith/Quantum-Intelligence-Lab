"""
test_statistics.py

Unit test for the Statistical Analyzer.
"""

from src.evaluation.statistical_analyzer import (
    StatisticalAnalyzer
)


def main():

    scores = [

        0.95,
        0.96,
        0.94,
        0.97,
        0.95

    ]

    analyzer = StatisticalAnalyzer()

    results = analyzer.analyze(
        scores
    )

    print()

    print("=" * 60)
    print("STATISTICAL ANALYSIS")
    print("=" * 60)

    for key, value in results.items():

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()