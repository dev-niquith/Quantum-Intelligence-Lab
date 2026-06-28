"""
comparison_matrix.py

Research Comparison Matrix

Converts benchmark results into:

- Rankings
- Tables
- CSV reports
"""

import pandas as pd


class ComparisonMatrix:

    def generate(self, results):

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="accuracy",
            ascending=False
        )

        df.insert(
            0,
            "rank",
            range(
                1,
                len(df) + 1
            )
        )

        return df

    def save_csv(
        self,
        dataframe,
        filepath
    ):

        dataframe.to_csv(
            filepath,
            index=False
        )

    def display(
        self,
        dataframe
    ):

        print("\n")
        print("=" * 60)
        print("RESEARCH COMPARISON MATRIX")
        print("=" * 60)

        print(
            dataframe[
                [
                    "rank",
                    "model",
                    "accuracy",
                    "f1"
                ]
            ]
        )