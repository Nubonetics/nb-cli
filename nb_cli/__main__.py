"""nb-cli is a command line tool created by Nubonetics."""
from nb_cli.cli import app
from nb_cli.system.app import system_app

app.add_typer(system_app, name="system")

if __name__ == "__main__":
    app()
