"""System commands."""
import typer

from nb_cli.cli import console
from nb_cli.system.fcn.info import system_info

system_app = typer.Typer()


# Commands
@system_app.command()
def info() -> None:
    """Display system information."""
    console.print(system_info())
