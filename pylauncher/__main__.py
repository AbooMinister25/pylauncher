"""
The entry point for the CLI. Invoked using `py` or `pylauncher`
"""
from pylauncher.core import PyLauncher

if __name__ == "__main__":
    cli = PyLauncher()
    cli.run()
