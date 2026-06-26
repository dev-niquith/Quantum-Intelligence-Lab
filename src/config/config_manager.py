"""
config_manager.py

Loads YAML configuration.
"""

import yaml


class ConfigManager:

    def __init__(
        self,
        config_path="configs/config.yaml"
    ):
        self.config_path = config_path

    def load(self):

        with open(
            self.config_path,
            "r"
        ) as file:

            return yaml.safe_load(file)