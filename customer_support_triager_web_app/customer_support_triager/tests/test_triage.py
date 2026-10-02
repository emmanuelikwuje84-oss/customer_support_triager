from app.triage.preprocessing import clean_text
from app.triage.rules import detect_rule_sentiment, detect_rule_urgency


def test_clean_text():
    assert clean_text("  Hello   WORLD  ") == "hello world"


def test_critical_urgency():
    assert detect_rule_urgency("my account was hacked") == "Critical"


def test_high_urgency():
    assert detect_rule_urgency("this is urgent") == "High"


def test_negative_sentiment():
    assert detect_rule_sentiment("this is terrible and frustrating") == "Negative"


def test_positive_sentiment():
    assert detect_rule_sentiment("thank you, this is excellent") == "Positive"
