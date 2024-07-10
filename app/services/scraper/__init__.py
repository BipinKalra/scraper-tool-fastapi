from aiohttp import ClientSession
from aiohttp_retry import RetryClient, RetryOptions
from .interfaces import Parser


class ScraperService:
    def __init__(self):
        self.client = RetryClient(raise_for_status=False, retry_options=RetryOptions(attempts=3, statuses=[404]))

    async def scrape_content(self, parser: Parser, url: str):
        try:
            async with self.client.get(url) as response:
                return await parser.parse(response.content)
        except:
            return []






