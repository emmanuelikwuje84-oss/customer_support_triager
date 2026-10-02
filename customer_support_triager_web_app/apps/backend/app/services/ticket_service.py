from uuid import uuid4

from sqlmodel import Session

from app.database.models import Ticket
from app.domains import get_domain
from app.llm.client import generate_response
from app.routing.router import route_ticket
from app.triage.engine import TriageEngine

triage_engine = TriageEngine()


def create_ticket(session, customer_name, domain_name, complaint):
    domain = get_domain(domain_name)

    if domain is None:
        raise ValueError("Unsupported domain.")

    analysis = triage_engine.analyze(complaint, domain)

    route = route_ticket(analysis["department"], domain)

    suggested_response = generate_response(
        complaint=complaint,
        department=analysis["department"],
        intent=analysis["intent"],
        urgency=analysis["urgency"],
        domain=domain,
    )

    ticket = Ticket(
        ticket_id=f"T-{uuid4().hex[:10].upper()}",
        customer_name=customer_name.strip(),
        domain=domain_name,
        complaint=complaint.strip(),
        cleaned_complaint=analysis["cleaned_complaint"],
        department=analysis["department"],
        intent=analysis["intent"],
        urgency=analysis["urgency"],
        sentiment=analysis["sentiment"],
        route=route,
        suggested_response=suggested_response,
    )

    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    return ticket
