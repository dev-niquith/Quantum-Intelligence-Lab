"""
reproduction_engine.py

Loads old experiment
configurations.
"""

import json


class ReproductionEngine:

    def __init__(
        self,
        database_connection
    ):
        self.connection = database_connection

    def load_experiment(
        self,
        experiment_id
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT config_snapshot
            FROM experiments
            WHERE id = ?
            """,
            (experiment_id,)
        )

        result = cursor.fetchone()

        if result:

            return json.loads(
                result[0]
            )

        return None