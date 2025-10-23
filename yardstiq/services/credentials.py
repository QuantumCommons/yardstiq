import keyring
import typer

_SERVICE_NAME = "yardstiq"


def set_token(provider_name: str, token: str):
    try:
        keyring.set_password(_SERVICE_NAME, provider_name, token)
        typer.secho(f"Token for '{provider_name}' registered.", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Keyring error: {e}", fg=typer.colors.RED)


def get_token(provider_name: str) -> str | None:
    try:
        return keyring.get_password(_SERVICE_NAME, provider_name)
    except Exception as e:
        typer.secho(f"Keyring error: {e}", fg=typer.colors.RED)
        return None


def delete_token(provider_name: str):
    try:
        keyring.delete_password(_SERVICE_NAME, provider_name)
        typer.secho(f"Token for '{provider_name}' removed.", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Keyring error: {e}", fg=typer.colors.RED)
