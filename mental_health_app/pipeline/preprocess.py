import pandas as pd
import re
import string
import os

RAW_DATA_PATH = "data/raw/social_media_posts.csv"
PROCESSED_DATA_PATH = "data/processed/cleaned_posts.csv"

def clean_text(text):
    """Remove punctuation, links, mentions, etc."""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)     # remove URLs
    text = re.sub(r"@\w+", "", text)        # remove mentions
    text = re.sub(r"#\w+", "", text)        # remove hashtags
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_data():
    """Load raw CSV, clean text, and save processed file."""
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"{RAW_DATA_PATH} not found.")
    
    df = pd.read_csv(RAW_DATA_PATH)
    df["cleaned_post"] = df["post"].astype(str).apply(clean_text)
    df.dropna(subset=["cleaned_post"], inplace=True)

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"✅ Preprocessed data saved to {PROCESSED_DATA_PATH}")
    return df

if __name__ == "__main__":
    preprocess_data()
