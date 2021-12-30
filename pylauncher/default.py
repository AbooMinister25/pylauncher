import sys

from pylauncher.config import get_installed_versions, set_default_version
from pylauncher.installer import compile_python, fetch_python, unzip_tar
from pylauncher.utils import confirm


def set_default(version) -> None:
    """
    Sets the default python version, and if not installed, installs it

    :return None:
    """

    if version not in get_installed_versions():
        confirm_install = confirm(
            f"Python version {version} not installed, do you want to install it?"
        )

        if confirm_install:
            temp_tarpath = fetch_python(version)
            unzip_tar(temp_tarpath)
            compile_python(version)

            print("Successfully downloaded python")

            set_default_version(
                version
            )  # Set the newly installed python version to the default
        else:
            print(f"Python version {version} does not exist")
            sys.exit(0)

    set_default_version(version)
