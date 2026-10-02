from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Ticket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ticket_id: str = Field(index=True)
    customer_name: str
    domain: str
    complaint: str
    cleaned_complaint: str
    department: str | None = None
    intent: str | None = None
    urgency: str | None = None
    sentiment: str | None = None
    route: str | None = None
    suggested_response: str | None = None
    status: str = "new"
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
