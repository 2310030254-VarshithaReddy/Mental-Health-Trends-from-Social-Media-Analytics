from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import pandas as pd
from schemas import AnalyticsResponse, DailyAgg

# Create FastAPI app
app = FastAPI(title="Mental Health Analytics API", version="1.0")

# ✅ Allow only your React frontend (port 3000)
origins = [
    "http://localhost:3000",  # React development server
    "http://127.0.0.1:3000",  # sometimes browsers resolve localhost differently
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Folder where processed analytics CSVs are stored
DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"


@app.get("/")
def root():
    return {"message": "Welcome to the Mental Health Analytics API"}


@app.get("/list")
def list_files():
    """
    Lists all available analytics files in data/processed directory.
    """
    files = [p.name for p in DATA_DIR.glob("analytics_*.csv")]
    return {"files": files}


@app.get("/analytics/{file_name}", response_model=AnalyticsResponse)
def get_analytics(file_name: str):
    """
    Returns daily aggregated sentiment data from a specific analytics CSV.
    """
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    df = pd.read_csv(file_path)

    # Convert rows to list of DailyAgg objects
    items = [
        DailyAgg(
            date_only=str(row["date_only"]),
            posts=int(row["posts"]),
            mean_vader=float(row["mean_vader"]),
            pos=int(row["pos"]),
            neg=int(row["neg"]),
        )
        for _, row in df.iterrows()
    ]

    return {"items": items}
