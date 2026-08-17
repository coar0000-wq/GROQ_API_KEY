#!/usr/bin/env python3
import os
import json
import asyncio
import aiohttp
import feedparser
from datetime import datetime
import google.generativeai as genai
import pathlib

# Obsidian vault ê²½ë¡œ (?™ì  ?¤ì •)
OBSIDIAN_VAULT = os.getenv('OBSIDIAN_VAULT', os.path.expanduser('~/Obsidian'))
OBSIDIAN_FOLDER = os.path.join(OBSIDIAN_VAULT, "JARVIS_LUNA_Data")
OUTPUT_FILE = "jarvis_luna_realtime.json"

# Gemini API ??(?„ìˆ˜)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("? ï¸ Warning: GEMINI_API_KEY environment variable not set. Using mock mode.")
    GEMINI_API_KEY = "mock-key-for-testing"

# Gemini ?´ë¼?´ì–¸??ì´ˆê¸°??try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    print(f"? ï¸ Warning: Could not initialize Gemini client: {e}")

async def fetch_youtube_realtime():
    """YouTube ?°ì´???˜ì§‘"""
    try:
        # ?”ë? ?°ì´??(?¤ì œë¡œëŠ” YouTube API ?¬ìš©)
        return [{
            "title": f"YouTube Video {datetime.now().strftime('%H:%M')}",
            "channel": "Channel Name",
            "url": "https://youtube.com"
        }]
    except Exception as e:
        print(f"YouTube ?¤ë¥˜: {e}")
        return []

async def fetch_arxiv_realtime():
    """arXiv ?¼ë¬¸ ?˜ì§‘"""
    try:
        feed = feedparser.parse('http://export.arxiv.org/rss/cs.AI?max_results=10')
        return [{
            "title": entry.get('title', 'No Title')[:100],
            "authors": entry.get('author', 'Unknown'),
            "url": entry.get('id', '')
        } for entry in feed.entries[:5]]
    except Exception as e:
        print(f"arXiv ?¤ë¥˜: {e}")
        return []

async def fetch_google_news_realtime():
    """Google News ?˜ì§‘"""
    try:
        feed = feedparser.parse('https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko')
        return [{
            "title": entry.get('title', 'No Title')[:100],
            "source": entry.get('source', {}).get('title', 'Unknown'),
            "url": entry.get('link', '')
        } for entry in feed.entries[:5]]
    except Exception as e:
        print(f"News ?¤ë¥˜: {e}")
        return []

def analyze_with_gemini(data, topic):
    """Gemini APIë¡?ë¶„ì„"""
    try:
        prompt = f"""?¤ìŒ {topic} ?°ì´?°ë? ê°„ë‹¨??ë¶„ì„?´ì£¼?¸ìš” (2-3ì¤?:
        {json.dumps(data, ensure_ascii=False, indent=2)}"""

        # Gemini API ?¸ì¶œ
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"? ï¸ Gemini ë¶„ì„ ?¤ë¥˜: {e}")
        return f"ë¶„ì„ ë¶ˆê? ({topic})"

def save_to_obsidian(youtube_data, arxiv_data, news_data):
    """Obsidian ?´ë”??markdown ?Œì¼ ?€??""
    try:
        # Obsidian ?´ë” ?ì„±
        obsidian_path = pathlib.Path(OBSIDIAN_FOLDER)
        obsidian_path.mkdir(parents=True, exist_ok=True)

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        # JARVIS LUNA ?¸ë±???˜ì´ì§€
        index_content = f"""---
title: JARVIS LUNA ?¤ì‹œê°??˜ì§‘
date: {date_str}
tags: [jarvis-luna, realtime, youtube, arxiv, news]
---

# ?¤– JARVIS LUNA ?¤ì‹œê°??°ì´??
**ë§ˆì?ë§??…ë°?´íŠ¸:** {time_str}

## ?“º YouTube
[[JARVIS LUNA YouTube {date_str}]]

## ?“„ arXiv
[[JARVIS LUNA arXiv {date_str}]]

## ?“° Google News
[[JARVIS LUNA News {date_str}]]

---
?ë™ ?ì„±?? JARVIS LUNA Gemini Edition
"""

        # YouTube ?˜ì´ì§€
        youtube_content = f"""---
title: JARVIS LUNA YouTube {date_str}
date: {date_str}
category: youtube
tags: [youtube, video, realtime]
---

# ?“º YouTube ?¤ì‹œê°??˜ì§‘

**?œê°„:** {time_str}

## ?°ì´??{json.dumps(youtube_data, ensure_ascii=False, indent=2)}

## ë¶„ì„
{analyze_with_gemini(youtube_data, 'YouTube ?ìƒ')}

---
[[JARVIS LUNA ?¤ì‹œê°??˜ì§‘]]
"""

        # arXiv ?˜ì´ì§€
        arxiv_content = f"""---
title: JARVIS LUNA arXiv {date_str}
date: {date_str}
category: arxiv
tags: [arxiv, papers, research]
---

# ?“„ arXiv ?¼ë¬¸ ?˜ì§‘

**?œê°„:** {time_str}

## ?°ì´??{json.dumps(arxiv_data, ensure_ascii=False, indent=2)}

## ë¶„ì„
{analyze_with_gemini(arxiv_data, 'arXiv ?¼ë¬¸')}

---
[[JARVIS LUNA ?¤ì‹œê°??˜ì§‘]]
"""

        # News ?˜ì´ì§€
        news_content = f"""---
title: JARVIS LUNA News {date_str}
date: {date_str}
category: news
tags: [news, google-news, realtime]
---

# ?“° Google News

**?œê°„:** {time_str}

## ?°ì´??{json.dumps(news_data, ensure_ascii=False, indent=2)}

## ë¶„ì„
{analyze_with_gemini(news_data, 'News')}

---
[[JARVIS LUNA ?¤ì‹œê°??˜ì§‘]]
"""

        # ?Œì¼ ?€??        (obsidian_path / "JARVIS_LUNA_?¤ì‹œê°??˜ì§‘.md").write_text(index_content, encoding='utf-8')
        (obsidian_path / f"JARVIS_LUNA_YouTube_{date_str}.md").write_text(youtube_content, encoding='utf-8')
        (obsidian_path / f"JARVIS_LUNA_arXiv_{date_str}.md").write_text(arxiv_content, encoding='utf-8')
        (obsidian_path / f"JARVIS_LUNA_News_{date_str}.md").write_text(news_content, encoding='utf-8')

        print(f"??Obsidian ?€???„ë£Œ: {obsidian_path}")
        return True
    except Exception as e:
        print(f"Obsidian ?€???¤ë¥˜: {e}")
        return False

async def main():
    """ë©”ì¸ ?¤í–‰ ?¨ìˆ˜"""
    print("?? JARVIS LUNA ?œì‘...")

    # ?°ì´???˜ì§‘
    youtube_data = await fetch_youtube_realtime()
    arxiv_data = await fetch_arxiv_realtime()
    news_data = await fetch_google_news_realtime()

    # JSON ?€??    data = {
        "timestamp": datetime.now().isoformat(),
        "youtube_data": youtube_data,
        "arxiv_data": arxiv_data,
        "google_news_data": news_data
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"??JSON ?€???„ë£Œ: {OUTPUT_FILE}")

    # Obsidian ?€??    save_to_obsidian(youtube_data, arxiv_data, news_data)

    print("??JARVIS LUNA ?„ë£Œ!")

if __name__ == "__main__":
    asyncio.run(main())
