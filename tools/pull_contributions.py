import sys
import json
import httpx
from lxml import html

USERNAME = "luckypushkarna"  # Fallback target

def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    resp = httpx.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"❌ Failed to fetch data: HTTP {resp.status_code}")
        sys.exit(1)
        
    tree = html.fromstring(resp.content)
    day_cells = tree.xpath("//td[@class='ContributionCalendar-day']")
    
    contributions = []
    for cell in day_cells:
        date = cell.get("data-date")
        level = cell.get("data-level", "0")
        if date:
            contributions.append({"date": date, "level": int(level)})
            
    with open("assets/contributions.json", "w", encoding="utf-8") as f:
        json.dump(contributions, f, indent=2)
    print(f"✅ Scraped {len(contributions)} days of contributions.")

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else USERNAME
    fetch_contributions(user)
