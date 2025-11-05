import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import joblib
from pipeline.preprocess import clean_text

PROCESSED_PATH = "data/processed/cleaned_posts.csv"
OUTPUT_PATH = "data/outputs/analysis_results.csv"  # ⬅️ changed path
MODEL_PATH = "models/classifier.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

def analyze_data():
    """Use trained model to predict sentiment of posts."""
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError("Model or vectorizer not found. Run train_model.py first.")

    df = pd.read_csv(PROCESSED_PATH)
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    df["cleaned_post"] = df["post"].astype(str).apply(clean_text)
    X_vec = vectorizer.transform(df["cleaned_post"])
    df["predicted_sentiment"] = model.predict(X_vec)
    df["sentiment_label"] = df["predicted_sentiment"].map({0: "Normal", 1: "Distressed"})

    # ✅ Save output to data/outputs
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Sentiment analysis saved to {OUTPUT_PATH}")

    # ✅ Optional summary printout
    print("\n📊 Sentiment Summary:")
    print(df["sentiment_label"].value_counts())

if __name__ == "__main__":
    analyze_data()
