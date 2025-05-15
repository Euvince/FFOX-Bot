Analyse de markdown
HTML -> CLean Markdown -> LLM (khaliq) -> Extract Links -> Send Requests -> CLean Markdown -> LLM -> Conditions -> True -> Save to Baserow

Logging (Redis)

Conditions:
1. Date: "Start date et end date"
2. primary keywords "all is must"
3. secondary keywords "all is not a must"

start_date: today 
end_date: 15-05-2023
primary_Keyword: name, school
secondary_keyword: is, you

Article:
pubslished date: 15-05-2025
My name is Khaliq


Logging

for link in links:
    send_to_redis({
        'scraping': [f'Link -> {link}']
    })

    send_to_redis({
        'scraping': [f'Link - Llm pasing -> {link}']
    })

    redis.expire(36000)



/get-log
redis.get('link_scraping')



/------------------------
Scraping: (httpx, html2text)

def clean_markdown() -> str|None:
    pass

def extract_links() -> list[str]:
    pass

25 links

async def send_requests() -> str|None:
    pass


async def start_processing() -> list[str]:
    asyncio.to_thread(clean_markdown())


Logging: (redis)
def log_to_redis(content: str) -> None:
    log_client.set(content)


scraping
