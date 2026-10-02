from app.llm.client import analyze_ticket
from app.ml.classifier import DepartmentMLClassifier
from app.triage.preprocessing import clean_text
from app.triage.rules import detect_rule_sentiment, detect_rule_urgency


class TriageEngine:
    def __init__(self):
        self.ml_classifier = DepartmentMLClassifier()

    def analyze(self, complaint, domain):
        cleaned = clean_text(complaint)

        rule_urgency = detect_rule_urgency(cleaned)
        rule_sentiment = detect_rule_sentiment(cleaned)
        ml_department = self.ml_classifier.predict(cleaned)

        llm_result = analyze_ticket(cleaned, domain)

        department = (
            ml_department
            if ml_department in domain["departments"]
            else llm_result["department"]
        )

        return {
            "cleaned_complaint": cleaned,
            "department": department,
            "intent": llm_result["intent"],
            "urgency": rule_urgency or llm_result["urgency"],
            "sentiment": rule_sentiment or llm_result["sentiment"],
        }
