def route_ticket(department, domain):
    return domain["teams"].get(
        department,
        domain["teams"].get("General", "General Support Team"),
    )
