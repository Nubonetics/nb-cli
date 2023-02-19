"""System commands."""
from typing import Optional

import typer

from nb_cli.cli import console
from nb_cli.system.properties import SystemProperties


twitter_app = typer.Typer()


@twitter_app.command()
def properties() -> None:
    """Display system properties."""
    console.print("System properties")
    SystemProperties()
