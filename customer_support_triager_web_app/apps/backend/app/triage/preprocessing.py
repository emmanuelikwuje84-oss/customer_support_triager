import re


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Complaint must be a string.")

    text = text.strip().lower()
    return re.sub(r"\s+", " ", text)
