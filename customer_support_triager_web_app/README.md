# Customer Support Ticket Triager

## Overview
This project is a small FastAPI-based customer support triage web app. A user submits a complaint, the backend cleans and classifies it, routes it to a likely team, and returns a suggested response. The frontend is a simple static HTML/CSS/JavaScript interface that communicates with the API.

## Features
- Ticket submission form for customer name, domain, and complaint text
- Domain-specific ticket routing for Banking, Healthcare, and Telecom
- Rule-based urgency and sentiment checks
- Department classification with a small scikit-learn model when a trained model exists
- OpenAI-backed analysis and response generation when an API key is configured
- SQLite persistence for saved tickets
- Health and organization endpoints for the frontend

## Architecture
Customer
  |
  v
Static frontend (HTML/CSS/JS)
  |
  v
FastAPI backend
  |-> Ticket validation and API routes
  |-> Business logic and triage workflow
  |-> Domain routing and classification
  |-> OpenAI integration for analysis/response
  |
  v
SQLite database and data files

## Project Structure
```text
customer_support_triager_web_app/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── apps/
│   ├── backend/
│   │   ├── app/
│   │   └── tests/
│   └── frontend/
│       ├── css/
│       ├── js/
│       └── index.html
├── data/
│   ├── training.csv
│   └── models/
├── docs/
├── scripts/
└── .venv/
```

The backend package remains under `apps/backend/app`, while the static frontend lives under `apps/frontend`. The environment file is stored at the repository root, not inside the frontend.

## Technologies
- Python 3
- FastAPI
- SQLModel
- SQLite
- scikit-learn
- python-dotenv
- OpenAI Python SDK
- HTML/CSS/JavaScript
- pytest

## Run Locally
Run these commands from the directory containing this README. If you have just
opened the repository root, enter the project directory first:

```bash
cd customer_support_triager_web_app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Open the repo-root `.env` file in your editor and replace
`your_api_key_here` with your OpenAI API key. Do not put `.env` in
`apps/frontend`. The app can start without an API key, but submitting tickets
requires one because ticket analysis and suggested responses use the OpenAI API.

Start the web app from the project directory:

```bash
python -m uvicorn --app-dir apps/backend app.main:app --reload
```

Open http://127.0.0.1:8000. API documentation is available at
http://127.0.0.1:8000/docs. Leave the server running in this terminal; press
`Ctrl+C` to stop it.

## Environment Variables
The app reads configuration from the repository-root `.env` file.

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5
DATABASE_URL=sqlite:///./data/support.db
```

The frontend does not contain or rely on a `.env` file.

## Testing
From the project directory, with the virtual environment activated:

```bash
cd apps/backend
python -m pytest tests -q
```

## API Endpoints
- `GET /api/health/` — returns service health status
- `GET /api/organizations/` — returns available domains and organization metadata
- `POST /api/tickets/` — submits a ticket payload with customer name, domain, and complaint

### Ticket request example
```json
{
  "customer_name": "Jane Doe",
  "domain": "banking",
  "complaint": "My account was hacked and I need immediate help."
}
```

### Ticket response example
```json
{
  "ticket_id": "T-123ABC",
  "customer_name": "Jane Doe",
  "domain": "banking",
  "department": "Security",
  "intent": "Fraud",
  "urgency": "Critical",
  "sentiment": "Negative",
  "route": "Security Team",
  "suggested_response": "Thank you for reporting this. We are escalating this to our security team immediately."
}
```

## Classification Logic
The project currently uses a hybrid approach:
- text cleaning and rule-based urgency/sentiment detection from keyword matching
- a scikit-learn model for department prediction when a trained model file exists
- OpenAI response generation and analysis when `OPENAI_API_KEY` is available

This means the classification is not purely ML-driven, and the system intentionally falls back to a rules-based and API-based path depending on configuration.

## Security
- `.env` is ignored by Git and never stored in the frontend app
- API keys are loaded from environment variables instead of being hardcoded in Python files
- the repository contains a `.env.example` file with placeholder values only
- database files and generated model artifacts are ignored in Git

## Development Notes
- The project is intentionally light-weight and suitable for a junior portfolio or internship project.
- The backend handles both the API and static frontend serving, which keeps deployment simple without a separate frontend framework.
- The data directory is shared at the repository root so backend configuration and model generation can use stable paths.

## Limitations
- keyword logic can miss unfamiliar phrasing or novel complaints
- rule-based sentiment and urgency checks are intentionally simple
- OpenAI availability and API quota affect response quality and analysis speed
- the model is only as good as the sample dataset in `data/training.csv`

## Future Improvements
- train a larger and better-labeled support dataset
- add evaluation metrics and model validation
- add database migrations and stronger persistence workflows
- add authentication and authorization
- add observability and monitoring
- split the frontend into a dedicated framework if the app grows
