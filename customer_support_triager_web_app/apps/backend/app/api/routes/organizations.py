from fastapi import APIRouter

from app.domains import DOMAINS

router = APIRouter(
    prefix="/api/organizations",
    tags=["Organizations"],
)


@router.get("/")
def get_organizations():
    return [
        {"id": name, "name": config["name"]}
        for name, config in DOMAINS.items()
    ]
