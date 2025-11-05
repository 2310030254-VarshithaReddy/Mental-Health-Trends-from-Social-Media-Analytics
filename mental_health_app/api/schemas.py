# api/schemas.py
from pydantic import BaseModel
from typing import List

class DailyAgg(BaseModel):
    date_only: str        # date in YYYY-MM-DD format
    posts: int            # number of posts collected that day
    mean_vader: float     # average sentiment score
    pos: int              # positive post count
    neg: int              # negative post count

class AnalyticsResponse(BaseModel):
    items: List[DailyAgg]
