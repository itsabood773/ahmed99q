
import asyncio
import aiohttp  # Requires installing: pip install aiohttp
from random import randint

async def fetch_url(session, url):
    """Asynchronously fetches the content of a URL using aiohttp."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return await response.text()  # Or response.read() for binary data
    except aiohttp.ClientError as e:  # Catch connection errors and HTTP errors
        print(f"Error fetching {url}: {e}")
        return None


async def main():
    """Creates an aiohttp session and fetches multiple URLs concurrently."""
    urls = list()
    apis =["2EJrAnKbT0xPlxBXPZHEIUoUrPsgGbb9",
        "GcI8ISIJHtLr6p62ei6wYSkAhEKW2z7W"]#"f2sGrgZ1BUfKiJ0GHe1rAyZYj1iScjf8"]
    #ad ="https://www.effectiveratecpm.com/ca83bzpx98?key=dee9c6f3171b614287718132222041ad"
    ad ="https://www.profitableratecpm.com/teuxkz6n?key=d383ed058802a4b1efcdf969672c48d6"
    for api in apis:
        for _ in range(randint (3,5)):
            url = f"https://api.webscrapingapi.com/v2?api_key={api}&url={ad}&country=us&render_js=1"
            urls.append(url)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)  # Run all tasks concurrently

    # Process the results (optional)
    for i, result in enumerate(results):
        if result:
            print("proxy" in result)
        else:
            print(f"Failed to fetch {urls[i]}")


if __name__ == "__main__":
   for i in range (1000):
     print(i)
     asyncio.run(main())
