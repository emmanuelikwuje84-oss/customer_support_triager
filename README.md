# Customer Support Ticket Triager

This repository contains the FastAPI app in `customer_support_triager_web_app/`.
It is not a Django project, so it has no `manage.py` and does not use
`python manage.py check`.

## Run Locally

Run these commands from the repository root (`/workspaces/customer_support_triager`):

```bash
cd customer_support_triager_web_app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp -n .env.example .env
```

Open `customer_support_triager_web_app/.env` in your editor and replace
`your_api_key_here` with your OpenAI API key. The `.env` file belongs in
`customer_support_triager_web_app/`, never in `apps/frontend/`. The app starts
without an API key, but ticket submission requires one.

Start the app from `customer_support_triager_web_app/`:

```bash
python -m uvicorn --app-dir apps/backend app.main:app --reload
```

Open http://127.0.0.1:8000. API documentation is at http://127.0.0.1:8000/docs.
Stop the server with `Ctrl+C`.

## Tests

With the virtual environment active, from `customer_support_triager_web_app/`:

```bash
cd apps/backend
python -m pytest tests -q
```

See [customer_support_triager_web_app/README.md](customer_support_triager_web_app/README.md)
for architecture and API details.