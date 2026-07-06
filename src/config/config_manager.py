"""
config_manager.py

Quantum Intelligence Lab (QIL)

Configuration Manager

Responsibilities
----------------

✓ Load YAML configuration
✓ Provide nested configuration access
✓ Reload configuration
✓ Return complete configuration

Future (v2.0)
-------------

- Environment-specific configs
- CLI overrides
- Experiment-specific configs
- Validation
"""

from pathlib import Path

import yaml


class ConfigManager:
    """
    Central configuration manager.

    Loads the YAML configuration once and
    provides convenient access throughout
    the application.
    """

    def __init__(
        self,
        config_path="configs/config.yaml"
    ):

        self.config_path = Path(config_path)

        self.config = self._load()

    # -------------------------------------------------
    # Internal Loader
    # -------------------------------------------------

    def _load(self):
        """
        Load configuration file.
        """

        with open(

            self.config_path,

            "r",

            encoding="utf-8"

        ) as file:

            return yaml.safe_load(file)

    # -------------------------------------------------
    # Public API
    # -------------------------------------------------

    def reload(self):
        """
        Reload configuration from disk.
        """

        self.config = self._load()

    def get(
        self,
        key=None,
        default=None
    ):
        """
        Retrieve a configuration value.

        Examples
        --------

        config.get()

        config.get("dataset")

        config.get("dataset.name")

        config.get("cross_validation.folds")
        """

        if key is None:

            return self.config

        value = self.config

        for part in key.split("."):

            if isinstance(value, dict):

                value = value.get(part)

            else:

                return default

            if value is None:

                return default

        return value

    def __repr__(self):

        return (

            f"ConfigManager('{self.config_path}')"

        )