"""Application install commands."""
import typer

from nb_cli.cli import console

# Functions
from nb_cli.app.install.fcn.kubectl import install_kubectl

install_app = typer.Typer()

# Commands
@install_app.command()
def kubectl() -> None:
    """Display system information."""
    console.print(install_kubectl())
