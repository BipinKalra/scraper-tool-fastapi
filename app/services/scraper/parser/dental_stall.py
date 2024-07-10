from asyncio import StreamReader
from bs4 import BeautifulSoup
from typing import List
from ..interfaces import Parser
from ..models import Product

def scrape_page(page: bytes) -> List[Product]:
    soup = BeautifulSoup(markup = page)
    product_list = soup.find_all(name = "ul", class_ = "products columns-4")[0].find_all(name = "li", class_ = "product")

    return [
        Product(
            title = product.findChild(name = "div", class_ = "mf-product-details").findChild(name = "a").getText(),
            image = product.findChild(name = "div", class_ = "mf-product-thumbnail").findChild(name = "img").get("data-lazy-src"),
            price = product.findChild(name = "div", class_ = "mf-product-details").findChild(name = "span", class_ = "woocommerce-Price-amount amount").findChild(name = "bdi").getText()
        )
        for product in product_list
    ]


class DentalStallParser(Parser):
    async def parse(self, stream: StreamReader) -> List[Product]:
        return scrape_page(await stream.read())

