"""nb-cli is a command line tool created by Nubonetics."""
from nb_cli.app.app import app_app
from nb_cli.cli import app
from nb_cli.system.app import system_app

app.add_typer(system_app, name="system")
app.add_typer(app_app, name="app")

if __name__ == "__main__":
    app()
