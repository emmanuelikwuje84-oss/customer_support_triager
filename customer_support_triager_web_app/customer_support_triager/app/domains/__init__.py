from app.domains.banking import DOMAIN as BANKING
from app.domains.healthcare import DOMAIN as HEALTHCARE
from app.domains.telecom import DOMAIN as TELECOM

DOMAINS = {
    "banking": BANKING,
    "healthcare": HEALTHCARE,
    "telecom": TELECOM,
}


def get_domain(domain_name: str):
    return DOMAINS.get(domain_name.lower())
