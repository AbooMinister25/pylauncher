import typer
import requests

from pylauncher.installer import unzip_tar, compile_python


app = typer.Typer()


@app.command
def install(version: str) -> None:
    """
    Downloads the provided python version from python.org/ftp

    :param version: The version to install
    :return: None
    """

    url = f"https://www.python.org/ftp/python/{version}/Python-{version}.tgz"

    response = requests.get(url)

    temp_tarpath = f"~/.pylauncher/temp/py_{version}.tgz"

    if response.status_code == 200:
        with open(temp_tarpath, "wb") as f:
            f.write(response.content)
    elif response.status_code == 404:
        typer.echo(f"Python version {version} does not exist", err=True)
        raise typer.Exit(code=1)
    else:
        typer.echo("Unexpected error occurred while downloading python", err=True)
        raise typer.Exit(code=1)

    unzip_tar(temp_tarpath)  # Unzip the downloaded tar file
    compile_python(version)  # Compile the newly downloaded python version

    typer.echo("Successfully downloaded python")
