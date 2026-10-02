CRITICAL_TERMS = [
    "hacked", "account takeover", "data breach",
    "identity theft", "life threatening",
    "life-threatening", "emergency",
]

HIGH_TERMS = [
    "fraud", "unauthorized", "unauthorised",
    "stolen", "urgent", "cannot access", "can't access",
]

NEGATIVE_TERMS = [
    "angry", "frustrated", "terrible", "bad",
    "worst", "fraud", "scam", "disappointed", "complaint",
]

POSITIVE_TERMS = [
    "thank", "thanks", "great", "excellent",
    "happy", "satisfied",
]


def detect_rule_urgency(text):
    for term in CRITICAL_TERMS:
        if term in text:
            return "Critical"

    for term in HIGH_TERMS:
        if term in text:
            return "High"

    return None


def detect_rule_sentiment(text):
    negative = sum(1 for term in NEGATIVE_TERMS if term in text)
    positive = sum(1 for term in POSITIVE_TERMS if term in text)

    if negative > positive:
        return "Negative"

    if positive > negative:
        return "Positive"

    return None
