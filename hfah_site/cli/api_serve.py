"""Render deploy: code-lab API only (no web UI). Pair with Hostinger static site."""
from __future__ import annotations

import os
from functools import partial
from http.server import ThreadingHTTPServer

import click

from hfah_site.cli.learn_ui import SITE_ROOT, _StudioHandler, _cors_origin, _ensure_project_context, _required_api_key


@click.command()
@click.option("--port", default=None, type=int, help="Port (Render sets $PORT).")
@click.option("--host", default=None, help="Bind address (default 0.0.0.0 on Render).")
def main(port: int | None, host: str | None) -> None:
    """Serve /api/* for the hosted learn site (static UI lives on Hostinger)."""
    _ensure_project_context()
    host = host or ("0.0.0.0" if os.environ.get("PORT") else "127.0.0.1")
    listen_port = port or int(os.environ.get("PORT", "8765"))

    _StudioHandler.api_only = True
    handler = partial(_StudioHandler, directory=str(SITE_ROOT))
    httpd = ThreadingHTTPServer((host, listen_port), handler)

    click.echo(f"Code lab API: http://{host}:{listen_port}/api/")
    if _required_api_key():
        click.echo("API key: required (X-HFAH-Key header)")
    if _cors_origin():
        click.echo(f"CORS origin: {_cors_origin()}")
    click.echo("Endpoints: GET /api/config, GET /api/snapshot, GET /api/pairs-snapshot, POST /api/run")
    click.echo("Not financial advice. Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        click.echo("\nStopped.")


if __name__ == "__main__":
    main()
