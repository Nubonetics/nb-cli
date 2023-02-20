"""System commands."""
import typer

from nb_cli.cli import console
from nb_cli.system.properties import system_properties

system_app = typer.Typer()


@system_app.command()
def properties() -> None:
    """Display system properties."""
    console.print(system_properties())
