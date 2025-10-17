from fastapi import FastAPI
from app.summarizer import get_summarized_news

app = FastAPI(title="AI News Summarizer API")

@app.get("/news")
def summarize_news(limit: int = 5):
    """Hacker News'ten ilk N haberi alır ve özetler"""
    results = get_summarized_news(limit)
    return {"news": results}
