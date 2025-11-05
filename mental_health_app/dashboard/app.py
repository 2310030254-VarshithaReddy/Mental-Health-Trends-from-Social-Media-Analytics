import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ---- PAGE SETUP ----
st.set_page_config(page_title="Mental Health Analytics Dashboard", layout="wide")

st.title("🧠 Mental Health Trends from Social Media Analytics")
st.markdown("This dashboard visualizes sentiment trends and mental health discussions from social media data.")

# ---- BACKEND CONNECTION ----
API_URL = "http://127.0.0.1:8000"  # Your FastAPI backend

# Fetch welcome message from backend
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        st.success("Connected to backend API successfully!")
    else:
        st.warning("Could not connect to API. Check if it's running.")
except Exception as e:
    st.error(f"API connection failed: {e}")

# ---- SAMPLE / DUMMY DATA ----
# In a real scenario, you would fetch this from your backend endpoint like /analyze or /trends
data = {
    "date": pd.date_range(start="2025-01-01", periods=10),
    "positive": [60, 70, 65, 75, 80, 78, 85, 90, 88, 92],
    "negative": [40, 30, 35, 25, 20, 22, 15, 10, 12, 8],
}
df = pd.DataFrame(data)
df["neutral"] = 100 - (df["positive"] + df["negative"]) / 2

st.subheader("📊 Sentiment Trends Over Time")
st.line_chart(df.set_index("date")[["positive", "negative", "neutral"]])

# ---- INSIGHTS ----
st.subheader("🩵 Key Insights")
col1, col2, col3 = st.columns(3)
col1.metric("Average Positive Sentiment", f"{df['positive'].mean():.1f}%")
col2.metric("Average Negative Sentiment", f"{df['negative'].mean():.1f}%")
col3.metric("Most Recent Positivity", f"{df['positive'].iloc[-1]}%")

# ---- VISUALIZATION: Correlation Heatmap ----
st.subheader("📈 Sentiment Correlation")
fig, ax = plt.subplots(figsize=(6, 3))
sns.heatmap(df[["positive", "negative", "neutral"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.markdown("---")
st.caption("Built with ❤️ using FastAPI + Streamlit")
