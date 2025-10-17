import requests
import time
from app.config import Config

def get_top_tech_stories(limit=10):
    one_week_ago = int(time.time()) - 7*24*3600
    query = "software"

    url = f"https://hn.algolia.com/api/v1/search?query={query}&tags=story&numericFilters=created_at_i>{one_week_ago}&hitsPerPage=1000"

    res = requests.get(url).json()
    hits = res.get("hits", [])

    if not hits:
        print("Algolia API: Bu query için hiç hikaye yok.")
    
    top_hits = sorted(hits, key=lambda x: x.get("points", 0), reverse=True)[:limit]

    top_stories = []
    for hit in top_hits:
        top_stories.append({
            "title": hit.get("title"),
            "url": hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
            "created_at": hit.get("created_at"),
            "author": hit.get("author"),
            "points": hit.get("points")
        })
    return top_stories



def summarize_with_openrouter(text):
    """OpenRouter modelini kullanarak kısa bir özet oluşturur"""
    headers = {
        "Authorization": f"Bearer {Config.OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "z-ai/glm-4.5-air:free",
        "messages": [
            {"role": "system", "content": "Summarize the following text briefly and clearly:"},
            {"role": "user", "content": text}
        ],
        "temperature": 0.7
    }
    
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        try:
            summary = data["choices"][0]["message"]["content"]
        except KeyError:
            summary = "No summary available."
        return summary.strip()
    else:
        return f"API error: {response.status_code}"


def get_summarized_news(limit=10):
    """Son 1 haftanın teknoloji hikayelerini alır ve özetler"""
    stories = get_top_tech_stories(limit)
    summarized = []
    for story in stories:
        summary = summarize_with_openrouter(story["title"])
        summarized.append({
            "title": story["title"],
            "summary": summary,
            "url": story["url"],
            "points": story["points"],
            "author": story["author"],
            "created_at": story["created_at"]
        })
    return summarized
