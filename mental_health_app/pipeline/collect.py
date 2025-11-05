import pandas as pd
import os

RAW_DATA_PATH = "data/raw/social_media_posts.csv"

def collect_data():
    """
    Loads raw social media posts data.
    In a real system, this could pull from APIs or scraped data.
    """
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"{RAW_DATA_PATH} not found. Please add your CSV file.")
    
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"✅ Loaded {len(df)} posts from {RAW_DATA_PATH}")
    return df

if __name__ == "__main__":
    collect_data()
