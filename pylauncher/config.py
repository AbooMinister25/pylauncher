import os
from pathlib import Path
from typing import List, Any
import toml


class Config:
    """The config class. Stores configuration information related to the launcher"""

    def __init__(self):
        self._config = self.load_config()

    def load_config(self) -> dict:
        """Loads and returns the configuration options for pylauncher"""

        config_dir = (
            os.environ.get("PYLAUNCHER_CONFIG_DIR")
            or f"{Path.home()}/.config/.pylauncher"
        )

        with open(config_dir, "r") as f:
            data = toml.load(f)

        # Set defaults
        data["CONFIG_DIR"] = config_dir

        return data

    def __getitem__(self, item: str) -> Any:
        return self._config[item]

    def __setitem__(self, key: str, value: str):
        self._config[key] = value

        with open(self["CONFIG_DIR"], "w") as f:
            toml.dump(self._config, f)  # Write updated config to file


config = Config()
