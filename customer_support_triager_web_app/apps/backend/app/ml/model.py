import csv

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from app.core.config import PROJECT_ROOT

DATA_PATH = PROJECT_ROOT / "data" / "training.csv"
MODEL_PATH = PROJECT_ROOT / "data" / "models" / "department_model.joblib"


def load_training_data():
    texts = []
    labels = []

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            texts.append(row["text"])
            labels.append(row["department"])

    return texts, labels


def train_model():
    texts, labels = load_training_data()

    pipeline = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
            ),
        ),
        (
            "classifier",
            LogisticRegression(max_iter=1000),
        ),
    ])

    pipeline.fit(texts, labels)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

    print("ML model trained successfully.")


if __name__ == "__main__":
    train_model()
