import os
from typing import List


class Config:
    """
    The config class. Stores configuration information related to the launcher
    """

    def __init__(self):
        self.CONFIG_DIR = (
            os.environ.get("PYLAUNCHER_CONFIG_DIR") or "~/.config/pylauncher"
        )
        self.CURRENT_VERSION = "python3.9"

    def get_installed_versions(self) -> List[str]:
        with open(f"{self.CONFIG_DIR}/.installed_versions", "r") as f:
            versions = f.readlines()

        return versions

    def set_default_version(self, version: str) -> None:
        with open(f"{self.CONFIG_DIR}/.python_version", "w") as f:
            f.write(version)

    def get_current_version(self) -> str:
        with open(f"{self.CONFIG_DIR}/.python-version", "r") as f:
            return f.read()


config = Config()
