from asyncio import gather
from fastapi import APIRouter, Depends
from itertools import chain
from typing import List
from db.repos.products import ProductsRepo
from services.scraper import ScraperService
from services.scraper.parser.dental_stall import DentalStallParser
from services.scraper.models import Product

router = APIRouter()

@router.get("/")
async def scrape(pages: int = 1) -> List[Product]:
    result = await gather(
        *[
            ScraperService().scrape_content(
                DentalStallParser(),
                f"https://dentalstall.com/shop/page/{page}/" if page > 1 else "http://localhost:8001/shop/"
            )

            for page in range(1, pages+1)
        ]
    )
    products = list(chain(*result))

    ProductsRepo().bulk_insert(products)
    return products
