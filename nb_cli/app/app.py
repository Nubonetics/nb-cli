"""Application commands."""
import typer

from nb_cli.app.install.app import install_app

app_app = typer.Typer()

app_app.add_typer(install_app, name="install")
