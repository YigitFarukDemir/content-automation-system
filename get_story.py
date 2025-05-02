import requests
import time

def get_top_weekly_stories(limit=5):
    one_week_ago = int(time.time()) - 7 * 24 * 60 * 60  # 7 gün önceki zaman (Unix)
    url = f"https://hn.algolia.com/api/v1/search?tags=story&numericFilters=created_at_i>{one_week_ago}&hitsPerPage=1000"

    res = requests.get(url).json()
    hits = res.get("hits", [])

    # Puanına göre sırala
    top_hits = sorted(hits, key=lambda x: x.get("points", 0), reverse=True)[:limit]

    top_stories = []
    for hit in top_hits:
        top_stories.append({
            "title": hit["title"],
            "url": hit["url"] or f"https://news.ycombinator.com/item?id={hit['objectID']}",
            "created_at": hit["created_at"],
            "author": hit["author"],
            "objectID": hit["objectID"],
            "points": hit["points"]
        })

    return top_stories
"""""
# Yazdır- print for test
weekly_stories = get_top_weekly_stories()
for i, story in enumerate(weekly_stories, start=1):
    print("top stories")
    print(f"{i}. {story['title']} ({story['points']} puan)")
    print(f"   {story['url']}")
    print(f"{story['created_at']} ({story['author']})\n")
"""

def get_cybersecurity_news(limit=5):
    one_week_ago = int(time.time()) - 7 * 24 * 3600
    url = f"https://hn.algolia.com/api/v1/search?query=cybersecurity&tags=story&numericFilters=created_at_i>{one_week_ago}&hitsPerPage=100"

    res = requests.get(url).json()
    hits = res.get("hits", [])

    # Puan sırasına göre ilk N tanesini al
    top_hits = sorted(hits, key=lambda x: x.get("points", 0), reverse=True)[:limit]

    return [
        {
            "title": hit["title"],
            "url": hit["url"] or f"https://news.ycombinator.com/item?id={hit['objectID']}",
            "created_at": hit["created_at"],
            "author": hit["author"],
            "objectID": hit["objectID"],
            "points": hit["points"]
        }
        for hit in top_hits
    ]
"""
# Yazdır- print for test
for i, story in enumerate(get_cybersecurity_news(), start=1):
    print("top cybersecurity stories")
    print(f"{i}. {story['title']} ({story['points']} puan)")
    print(f"   {story['url']}")
    print(f"{story['created_at']} ({story['author']})\n")
"""