import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# --- Step 1: Example dataset ---
# Replace this later with your real mental health dataset
data = {
    "text": [
        "I feel happy and motivated today",
        "Life is beautiful and I love myself",
        "I am feeling very depressed and hopeless",
        "Everything is falling apart, I can't focus",
        "I’m anxious about the future",
        "I feel calm and relaxed after meditation"
    ],
    "label": [0, 0, 1, 1, 1, 0]  # 0 = Normal, 1 = Distressed
}
df = pd.DataFrame(data)

# --- Step 2: Split data ---
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# --- Step 3: Text vectorization ---
vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)

# --- Step 4: Train model ---
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# --- Step 5: Save model and vectorizer ---
joblib.dump(model, "models/classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model and vectorizer saved successfully in the models/ folder.")
