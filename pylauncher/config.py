import os
import pathlib

CONFIG_DIR = os.environ.get("PYLAUNCHER_CONFIG_DIR") or "~/.config/pylauncher"
CURRENT_VERSION = "python3.9"

def get_installed_versions() -> list[str]:
    with open(f"{CONFIG_DIR}/.installed_versions", "r") as f:
        versions = f.readlines()

    return versions


def set_default_version(version: str) -> None:
    with open(f"{CONFIG_DIR}/.python_version", "w") as f:
        f.write(version)


def get_current_version() -> str:
    with open(f"{CONFIG_DIR}/.python-version", "r") as f:
        return f.read()
