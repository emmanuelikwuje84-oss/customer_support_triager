import os
from pathlib import Path

from dotenv import load_dotenv


def find_project_root(start_path: Path) -> Path:
    for candidate in (start_path, *start_path.parents):
        if (candidate / "apps").exists() and (candidate / "data").exists():
            return candidate
    return start_path


def normalize_database_url(raw_url: str | None) -> str:
    if not raw_url or not raw_url.startswith("sqlite"):
        return raw_url or "sqlite://"

    if raw_url.startswith("sqlite:////"):
        return raw_url

    if raw_url.startswith("sqlite:///"):
        relative_path = raw_url.removeprefix("sqlite:///")
        if relative_path.startswith("./"):
            relative_path = relative_path[2:]
        return f"sqlite:///{(PROJECT_ROOT / relative_path).as_posix()}"

    return raw_url


PROJECT_ROOT = find_project_root(Path(__file__).resolve())
load_dotenv(PROJECT_ROOT / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")
DATABASE_PATH = PROJECT_ROOT / "data" / "support.db"
DATABASE_URL = normalize_database_url(
    os.getenv(
        "DATABASE_URL",
        f"sqlite:///{DATABASE_PATH.as_posix()}",
    )
)
