from typing import List
from fastapi import APIRouter
from services.scraper.models import Product
from db.repos.products import ProductsRepo

router = APIRouter()

@router.get("/")
def get_products() -> List[Product]:
    return ProductsRepo().get_all()

@router.get("/{product_id}/")
def get_product(product_id: int) -> Product:
    return ProductsRepo().get_by_id(product_id)
