from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes.health import router as health_router
from app.api.routes.organizations import router as organizations_router
from app.api.routes.tickets import router as tickets_router
from app.core.config import PROJECT_ROOT
from app.database.database import create_tables

DATA_DIR = PROJECT_ROOT / "data"
FRONTEND_DIR = PROJECT_ROOT / "apps" / "frontend"


@asynccontextmanager
async def lifespan(app: FastAPI):
    DATA_DIR.mkdir(exist_ok=True)
    create_tables()
    yield


app = FastAPI(
    title="Customer Support Triage Engine",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(organizations_router)
app.include_router(tickets_router)

app.mount(
    "/",
    StaticFiles(directory=str(FRONTEND_DIR), html=True),
    name="frontend",
)
