# Hedge Fund at Home — Render API (public)

Public **API-only** service for the learn site Code lab. Deploy on Render; pair with the private static UI on Hostinger.

- **No `web/` UI** in this repo — visitors use your custom domain for the site.
- Depends on the public [hedge-fund-at-home](https://github.com/ashlynbain/hedge-fund-at-home) toolkit at runtime.

## Render

Connect this repo in Render → **Blueprint** → `render.yaml`.

Set `HFAH_CORS_ORIGIN` to your site, e.g. `https://hedgefunddiy.ashlynbain.com`.

## Local API smoke test

```bash
git clone https://github.com/ashlynbain/hedge-fund-at-home.git ../hedge-fund-at-home
pip install -e "../hedge-fund-at-home[dev]" -e ".[dev]"
export HFAH_TOOLKIT_ROOT=../hedge-fund-at-home
export HFAH_CONFIG=../hedge-fund-at-home/config/config.yaml.example
python -m hfah_site.cli.api_serve
curl http://127.0.0.1:8765/api/config
```
