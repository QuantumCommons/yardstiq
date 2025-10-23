import typer
from ..core.impl import qpu_impl

app = typer.Typer(
    name="qpu", help="Manage and list available QPUs.", no_args_is_help=True
)


@app.command("ls")
def list_qpus():
    """Lists all discovered QPUs (installed and local)."""

    typer.echo("Available QPUs:")
    qpus = qpu_impl.list_available_qpus()

    if not qpus:
        typer.echo("  No QPUs found.")
        return

    for name in qpus:
        typer.echo(f"- {typer.style(name, bold=True)}")
