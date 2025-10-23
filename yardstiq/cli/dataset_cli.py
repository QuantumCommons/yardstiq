import typer
from ..core.impl import dataset_impl

app = typer.Typer(
    name="dataset", help="Manage and list available Datasets.", no_args_is_help=True
)


@app.command("ls")
def list_datasets():
    """Lists all discovered Datasets (installed and local)."""

    typer.echo("Available Datasets:")
    datasets = dataset_impl.list_available_datasets()

    if not datasets:
        typer.echo("  No datasets found.")
        return

    for name in datasets:
        typer.echo(f"- {typer.style(name, bold=True)}")
