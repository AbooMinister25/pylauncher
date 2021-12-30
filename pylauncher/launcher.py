from typing import List

import subprocess

from pylauncher.config import CURRENT_VERSION


def run_python(*options: str) -> None:
    subprocess.run([CURRENT_VERSION, *options])
