import subprocess

from pylauncher.config import config


def run_python(*options: str) -> None:
    subprocess.run([config.CURRENT_VERSION, *options])
