import tarfile
from pathlib import Path
import subprocess


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
