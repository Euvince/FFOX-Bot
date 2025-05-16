import httpx
import asyncio
from typing import List
from clean_markdown import clean_markdown
from extract_links import extract_links


async def fetch_html(link: str, client: httpx.AsyncClient) -> str:
    print(f"\n🔄 SCRAPING: {link}")
    try:
        response = await client.get(link, timeout=10.0)
        if response.status_code == 200 and "text/html" in response.headers.get("content-type", ""):
            print(f"✅ SUCCESS: {link}")
            return response.text
    except httpx.RequestError as e:
        print(f"❌ ERROR: {link} -> {e}")
    return ""


async def send_requests(links: List[str]) -> List[str]:
    markdowns = []
    async with httpx.AsyncClient() as client:
        tasks = [fetch_html(link, client) for link in links]
        html_contents = await asyncio.gather(*tasks)

        for html in html_contents:
            if html:
                markdowns.append(clean_markdown(html))
    return markdowns


async def main():
    links = extract_links()
    results = await send_requests(links)

    for md in results:
        print(md)

if __name__ == "__main__":
    asyncio.run(main())
