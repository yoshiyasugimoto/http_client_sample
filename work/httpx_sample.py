import asyncio

import httpx
from bs4 import BeautifulSoup


async def get(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    text = r.text
    html = BeautifulSoup(text, "html.parser")
    print(html)


if __name__ == "__main__":
    asyncio.run(get("https://churadata.okinawa/"))
