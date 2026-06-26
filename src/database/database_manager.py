"""
database_manager.py

Database manager for QIL.
"""

import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        self.db_path = (
            Path("experiments")
            / "qil_experiments.db"
        )

        self.connection = sqlite3.connect(
            self.db_path
        )

    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS experiments (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            dataset_name TEXT,

            experiment_type TEXT,

            random_seed INTEGER,

            version TEXT,

            num_samples INTEGER,

            num_features INTEGER,

            qml_suitability_score INTEGER,

            qri_score INTEGER,

            config_snapshot TEXT,

            notes TEXT
        )
        """)

        self.connection.commit()

    def close(self):

        self.connection.close()