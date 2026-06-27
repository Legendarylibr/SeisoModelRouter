"""Seiso Smart Router CLI."""

from __future__ import annotations

import typer

from seiso_cli.commands.router import router_serve

app = typer.Typer(
    name="seiso-router",
    help="Seiso Smart Router service.",
    no_args_is_help=True,
)

app.command("serve")(router_serve)
app.command("router")(router_serve)

if __name__ == "__main__":
    app()

