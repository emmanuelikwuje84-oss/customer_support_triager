# Customer Support Ticket Triager

A local web application for customer-support ticket triage.

The system accepts a complaint, analyzes it, classifies department, intent, urgency and sentiment, routes the ticket, generates a suggested response, and stores the ticket in SQLite.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your OpenAI API key.

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

API docs: http://127.0.0.1:8000/docs

## Train sample ML model

```bash
python -m app.ml.model
```

The included training CSV is only a small demonstration dataset. A serious model requires a real labeled dataset and proper evaluation.

## Test

```bash
pytest
```

Never commit `.env` or real API keys.
