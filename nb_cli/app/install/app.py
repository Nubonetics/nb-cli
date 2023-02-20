"""Application install commands."""
import typer

# Functions
from nb_cli.app.install.fcn.kubectl import install_kubectl
from nb_cli.cli import console

install_app = typer.Typer()


# Commands
@install_app.command()
def kubectl() -> None:
    """Display system information."""
    console.print(install_kubectl())
