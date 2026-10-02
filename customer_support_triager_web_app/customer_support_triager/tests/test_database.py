from app.database.models import Ticket


def test_ticket_defaults():
    ticket = Ticket(
        ticket_id="T-TEST",
        customer_name="Test User",
        domain="banking",
        complaint="Test complaint",
        cleaned_complaint="test complaint",
    )

    assert ticket.status == "new"
    assert ticket.department is None
