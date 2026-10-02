from pathlib import Path

import joblib

MODEL_PATH = Path("data/models/department_model.joblib")


class DepartmentMLClassifier:
    def __init__(self):
        self.model = None

        if MODEL_PATH.exists():
            self.model = joblib.load(MODEL_PATH)

    def predict(self, text):
        if self.model is None:
            return None

        return self.model.predict([text])[0]
