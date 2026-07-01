"""
comparison_matrix.py

Quantum Intelligence Lab (QIL)

Research Comparison Matrix

This module converts benchmark results into a
research-friendly leaderboard and exports the results.

Responsibilities
----------------

• Display ranked benchmark results.
• Save benchmark results as CSV.
• Act as the reporting layer between the benchmark engine
  and future modules such as:

    - Publication Generator
    - Recommendation Engine
    - AI Research Copilot
"""

from pathlib import Path

import pandas as pd


class ComparisonMatrix:
    """
    Research Comparison Matrix.
    """

    def __init__(self):

        self.output_directory = Path("reports")

        self.output_directory.mkdir(
            exist_ok=True
        )

    def generate(
        self,
        leaderboard: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Display and save the benchmark results.

        Parameters
        ----------
        leaderboard

            Ranked benchmark dataframe.

        Returns
        -------
        pandas.DataFrame
        """

        dataframe = leaderboard.copy()

        self.display(
            dataframe
        )

        self.save_csv(
            dataframe
        )

        return dataframe

    def display(
        self,
        dataframe: pd.DataFrame
    ):

        print()

        print("=" * 70)
        print("RESEARCH COMPARISON MATRIX")
        print("=" * 70)

        display_columns = [

            "rank",

            "model",

            "accuracy",

            "accuracy_std",

            "f1"

        ]

        print(

            dataframe[
                display_columns
            ].to_string(
                index=False
            )

        )

    def save_csv(
        self,
        dataframe: pd.DataFrame
    ):

        output_file = (

            self.output_directory /

            "benchmark_results.csv"

        )

        export_dataframe = dataframe.drop(
            columns=["full_statistics"],
            errors="ignore"
        )

        export_dataframe.to_csv(
            output_file,
            index=False
        )

        print()

        print(
            f"Research report saved to:\n{output_file}"
        )

    def top_model(
        self,
        dataframe: pd.DataFrame
    ):
        """
        Return the best performing model.
        """

        return dataframe.iloc[0]

    def summary(
        self,
        dataframe: pd.DataFrame
    ):

        best = self.top_model(
            dataframe
        )

        print()

        print("=" * 70)
        print("BENCHMARK SUMMARY")
        print("=" * 70)

        print(
            f"Best Model : {best['model']}"
        )

        print(
            f"Mean Accuracy : {best['accuracy']:.4f}"
        )

        print(
            f"Std Dev : {best['accuracy_std']:.4f}"
        )

        print(
            f"F1 Score : {best['f1']:.4f}"
        )