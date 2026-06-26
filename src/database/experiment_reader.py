"""
experiment_reader.py

Read experiment history.
"""

import pandas as pd


class ExperimentReader:

    def __init__(
        self,
        database_connection
    ):
        self.connection = database_connection

    def get_all_experiments(self):

        query = """
        SELECT *
        FROM experiments
        ORDER BY id DESC
        """

        return pd.read_sql_query(
            query,
            self.connection
        )