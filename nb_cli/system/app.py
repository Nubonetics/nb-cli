"""System commands."""
import typer

from nb_cli.cli import console
from nb_cli.system.fcn.info import system_info

system_app = typer.Typer()


@system_app.command()
def info() -> None:
    """Display system properties."""
    console.print(system_info())
