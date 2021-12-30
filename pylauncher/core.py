import argparse
import sys

from pylauncher.default import set_default
from pylauncher.installer import compile_python, fetch_python, unzip_tar
from pylauncher.launcher import run_python


class PyLauncher:
    def __init__(self):
        self.python_arguments = []  # Arguments to pass onto the python executable

        self.parser = argparse.ArgumentParser(
            description="A python launcher and version manager"
        )
        self.parser.add_argument(
            "command", help="Subcommand to run", nargs="?", default=None
        )

    def install(self) -> None:
        """
        Installs the provided python version

        :return: None
        """

        parser = argparse.ArgumentParser(
            description="Install the provided python version"
        )

        parser.add_argument("version", type=float, help="The python version to install")
        args, unknown = parser.parse_known_args(sys.argv[2:])
        version = args.version

        temp_tarpath = fetch_python(
            version
        )  # Install the python version from python.org
        unzip_tar(temp_tarpath)  # Unzip the downloaded tar file
        compile_python(version)  # Compile the newly downloaded python version

        print(f"Successfully installed python {version}")

        self.python_arguments.append(
            unknown
        )  # Add unknown args to be passed onto the main python executable

    def default(self) -> None:
        """
        Sets the default python version, and if not installed, installs it

        :return None:
        """

        parser = argparse.ArgumentParser(description="Set the default python version")

        parser.add_argument(
            "version", type=float, help="The python version to set as the default"
        )
        args, unknown = parser.parse_known_args(sys.argv[2:])
        version = args.version

        set_default(version)

        self.python_arguments.append(
            unknown
        )  # Add unknown args to be passed onto the main python executable

    def run_python(self) -> None:
        """
        Launches the python executable

        :return None:
        """
        run_python(*self.python_arguments)

    def run(self) -> None:
        """
        Runs the argument parser

        :return: None
        """

        if len(sys.argv) == 1:
            self.run_python()
            sys.exit(1)

        args, unknown = self.parser.parse_known_args(sys.argv[1:])
        self.python_arguments.extend(unknown)

        if args.command is None:
            self.run_python()
            return

        if not hasattr(self, str(args.command)):
            self.python_arguments.append(args.command)
            self.run_python()
            return

        subcommand = getattr(self, args.command)  # Dispatch to correct function

        subcommand()
        self.run_python()
