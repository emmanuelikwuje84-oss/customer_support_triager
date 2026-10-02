from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlmodel import Session

from app.database.database import get_session
from app.services.ticket_service import create_ticket

router = APIRouter(
    prefix="/api/tickets",
    tags=["Tickets"],
)


class TicketCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=120)
    domain: str = Field(min_length=1, max_length=50)
    complaint: str = Field(min_length=1, max_length=10000)


@router.post("/")
def submit_ticket(
    data: TicketCreate,
    session: Session = Depends(get_session),
):
    try:
        return create_ticket(
            session=session,
            customer_name=data.customer_name,
            domain_name=data.domain,
            complaint=data.complaint,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except RuntimeError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
