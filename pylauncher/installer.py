import subprocess
import sys
import tarfile
from pathlib import Path

import requests


def fetch_python(version: str) -> str:
    """
    Fetches the given python version from python.org

    :param version: The version to fetch.
    """

    url = f"https://www.python.org/ftp/python/{version}/Python-{version}.tgz"

    response = requests.get(url)

    temp_tarpath = f"~/.pylauncher/temp/py_{version}.tgz"

    if response.status_code == 200:
        with open(temp_tarpath, "wb") as f:
            f.write(response.content)
    elif response.status_code == 404:
        print(f"Python version {version} does not exist", file=sys.stderr)
        sys.exit(1)
    else:
        print("Unexpected error occurred while downloading python", file=sys.stderr)
        sys.exit(1)


def unzip_tar(path: str) -> None:
    """
    Unzips the given tarfile

    :param path: The path to the archive.
    :return: None
    """

    tar = tarfile.open(path)
    tar.extractall()
    tar.close()


def compile_python(version: str) -> None:
    """
    Compiles the installed python version

    :param version: The python version
    :return: None
    """
    source_path = Path.cwd() / f"Python-{version}"
    subprocess.run(
        [
            f"{source_path}/.configure",
            "--enable-optimizations",
            "--with-ensurepip=install",
        ]
    )
    subprocess.run(["make", "-j", "8"], cwd=source_path)
    subprocess.run("sudo make altinstall", shell=True, cwd=source_path)
