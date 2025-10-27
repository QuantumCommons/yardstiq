import typer

from ..core.impl import backend_impl

app = typer.Typer(
    name="backend", help="Manage and list available backends.", no_args_is_help=True
)


@app.command("ls")
def list_backends():
    """Lists all discovered backend (installed and local)."""

    typer.echo("Available backends:")
    backends = backend_impl.list_available_backends()

    if not backends:
        typer.echo("  No backend found.")
        return

    for name in backends:
        typer.echo(f"- {typer.style(name, bold=True)}")
