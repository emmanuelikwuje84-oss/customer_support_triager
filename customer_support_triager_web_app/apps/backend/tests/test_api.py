from fastapi.testclient import TestClient
import httpx
from openai import RateLimitError

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_organizations():
    response = client.get("/api/organizations/")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_ticket_quota_error_returns_json_message(monkeypatch):
    def reject_ticket(**kwargs):
        response = httpx.Response(
            429,
            request=httpx.Request(
                "POST", "https://api.openai.com/v1/responses"
            ),
        )
        raise RateLimitError(
            "quota exhausted",
            response=response,
            body={"error": {"message": "quota exhausted"}},
        )

    monkeypatch.setattr("app.api.routes.tickets.create_ticket", reject_ticket)
    response = client.post(
        "/api/tickets/",
        json={
            "customer_name": "Jane Doe",
            "domain": "banking",
            "complaint": "I need help with a payment.",
        },
    )

    assert response.status_code == 503
    assert response.json()["detail"] == (
        "OpenAI quota or rate limit reached. Check account billing and limits."
    )
