🧠 Mental Health Trends from Social Media Analytics
📋 Overview

This project analyzes mental health trends using social media data.
It collects, cleans, and analyzes text posts to identify emotional patterns, sentiment, and overall well-being trends.
The project also includes data visualization and model training for predictive insights.

🧩 Project Structure
mental_health_analytics/
│
├── data/
│   ├── raw/                   # Raw collected data
│   ├── processed/             # Cleaned and preprocessed data
│   └── cleaned_posts.csv      # Final dataset after preprocessing
│
├── models/
│   ├── train_model.py         # Model training script
│   └── saved_model.pkl        # Saved trained model (output)
│
├── pipeline/
│   ├── collect.py             # Data collection from sources (API, CSV, etc.)
│   ├── preprocess.py          # Data cleaning and text preprocessing
│   ├── analyze.py             # Data analysis and visualization
│   ├── train_model.py         # Optional training module for pipeline integration
│   ├── run_pipeline.py        # Runs all pipeline steps sequentially
│   └── run_all.sh             # Bash script to execute full pipeline
│
├── frontend/
│   └── (React or Streamlit App)  # Dashboard for visualization
│
├── .env                       # Environment variables
├── .gitignore                 # Files/folders to ignore in Git
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── venv/                      # Virtual environment (not tracked by Git)

⚙️ Setup Instructions
1️⃣ Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set up environment variables

Create a .env file in the project root:

API_KEY=your_api_key_here
DATA_SOURCE=twitter
MODEL_PATH=models/saved_model.pkl

🚀 Running the Pipeline
Run all scripts at once
python pipeline/run_pipeline.py

Or use the shell script
bash pipeline/run_all.sh

📊 Key Features

✅ Collects data from social media platforms
✅ Cleans and preprocesses text data
✅ Performs sentiment and trend analysis
✅ Trains a machine learning model for prediction
✅ Generates visual reports and dashboards

🧠 Example Use Case

Track anxiety and depression-related trends among students.

Identify the most discussed mental health topics weekly.

Analyze sentiment shifts over time.

📈 Future Improvements

Integrate real-time API streaming

Add topic modeling (LDA)

Expand to multi-language support

Connect with dashboard frontend