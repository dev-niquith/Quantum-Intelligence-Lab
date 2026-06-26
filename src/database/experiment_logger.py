"""
experiment_logger.py

Stores experiments.
"""

from datetime import datetime
import json


class ExperimentLogger:

    def __init__(
        self,
        database_connection
    ):
        self.connection = database_connection

    def log_experiment(
        self,
        dataset_name,
        report,
        config
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO experiments (

                timestamp,

                dataset_name,

                experiment_type,

                random_seed,

                version,

                num_samples,

                num_features,

                qml_suitability_score,

                qri_score,

                config_snapshot,

                notes

            )

            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,

            (
                datetime.now().isoformat(),

                dataset_name,

                "dataset_analysis",

                config[
                    "random_seed"
                ],

                "0.1.0",

                report[
                    "num_samples"
                ],

                report[
                    "num_features"
                ],

                report[
                    "qml_suitability_score"
                ],

                report[
                    "qri_score"
                ],

                json.dumps(config),

                "Dataset Analysis"
            )
        )

        self.connection.commit()