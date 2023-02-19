"""System commands."""
import typer

from nb_cli.cli import console
from nb_cli.system import SystemProperties

system_app = typer.Typer()


@system_app.command()
def properties() -> None:
    """Display system properties."""
    console.print("System properties")
    SystemProperties()
