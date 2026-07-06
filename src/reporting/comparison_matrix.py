"""
comparison_matrix.py

Quantum Intelligence Lab (QIL)

Research Comparison Matrix

Converts benchmark results into a unified
research leaderboard.

Responsibilities
----------------

✓ Generate research leaderboard
✓ Display benchmark rankings
✓ Export benchmark results
✓ Provide research summaries

Future Extensions (v2.0)
------------------------

- Publication Report Generator
- AI Recommendation Engine
- Research Copilot
- Interactive Dashboard
"""

from pathlib import Path
from datetime import datetime

import pandas as pd


class ComparisonMatrix:
    """
    Research Comparison Matrix.

    Responsible for formatting,
    displaying and exporting benchmark
    results.
    """

    def __init__(self):

        self.output_directory = Path("reports")

        self.output_directory.mkdir(
            exist_ok=True
        )

    # -------------------------------------------------
    # Generate Leaderboard
    # -------------------------------------------------

    def generate(
        self,
        leaderboard
    ):
        """
        Generate a ranked research leaderboard.

        Parameters
        ----------
        leaderboard

            Either

            • pandas DataFrame

            OR

            • list of dictionaries

        Returns
        -------
        pandas DataFrame
        """

        if isinstance(
            leaderboard,
            list
        ):

            dataframe = pd.DataFrame(
                leaderboard
            )

        else:

            dataframe = leaderboard.copy()

        if dataframe.empty:

            return dataframe

        dataframe = (

            dataframe

            .sort_values(

                by="accuracy",

                ascending=False

            )

            .reset_index(drop=True)

        )

        dataframe = dataframe.copy()

        if "rank" in dataframe.columns:

            dataframe = dataframe.drop(columns=["rank"])

        dataframe.insert(
            0,
            "rank",
            range(1, len(dataframe) + 1)
        )




        return dataframe

    # -------------------------------------------------
    # Display Leaderboard
    # -------------------------------------------------

    def display(
        self,
        dataframe
    ):
        """
        Display benchmark rankings.
        """

        print()

        print("=" * 70)
        print("RESEARCH COMPARISON MATRIX")
        print("=" * 70)

        columns = [

            "rank",

            "category",

            "model",

            "accuracy",

            "accuracy_std",

            "f1"

        ]

        available_columns = [

            column

            for column in columns

            if column in dataframe.columns

        ]

        print(

            dataframe[
                available_columns
            ].to_string(
                index=False
            )

        )

    # -------------------------------------------------
    # Export CSV
    # -------------------------------------------------

    def save_csv(
        self,
        dataframe,
        dataset_name="dataset"
    ):
        """
        Save benchmark results using a unique
        timestamped filename.

        Example
        -------
        breast_cancer_20260702_231055.csv
        """

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"{dataset_name}_{timestamp}.csv"
        )

        output_file = (
            self.output_directory /
            filename
        )

        export_dataframe = dataframe.drop(
            columns=["statistics"],
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

        return output_file


    # -------------------------------------------------
    # Best Model
    # -------------------------------------------------

    def top_model(
        self,
        dataframe
    ):
        """
        Return the best model.
        """

        if dataframe.empty:

            return None

        return dataframe.iloc[0]

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    def summary(
        self,
        dataframe
    ):
        """
        Print research summary.
        """

        best = self.top_model(
            dataframe
        )

        if best is None:

            return

        print()

        print("=" * 70)
        print("RESEARCH SUMMARY")
        print("=" * 70)

        print(
            f"Best Model      : {best['model']}"
        )

        print(
            f"Category        : {best['category']}"
        )

        print(
            f"Mean Accuracy   : "
            f"{best['accuracy']:.4f}"
        )

        print(
            f"Std Deviation   : "
            f"{best['accuracy_std']:.4f}"
        )

        print(
            f"F1 Score        : "
            f"{best['f1']:.4f}"
        )

        if "training_time" in dataframe.columns:

            print(
                f"Training Time   : "
                f"{best['training_time']:.4f} sec"
            )