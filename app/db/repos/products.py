import json
from pathlib import Path
from typing import List
from services.scraper.models import Product


class ProductsRepo:
    def bulk_insert(self, products: List[Product]):
        db_path = Path.cwd() / "app" / "db" / "data" / "products.json"
        with open(db_path, "r") as file:
            try:
                current = json.load(file)
            except json.JSONDecodeError:
                current = []

        with open(db_path, "w+") as file:
            updated = [product.__dict__ for product in products]

            current_by_title = {product["title"]: product for product in current}
            for row in updated:
                if row["title"] not in current_by_title:
                    current.append(row)
                elif row["price"] != current_by_title[row["title"]]["price"]:
                    current_by_title[row["title"]]["price"] = row["price"]

            json.dump(
                current,
                file,
            )

    def get_by_id(self, id) -> Product:
        db_path = Path.cwd() / "app" / "db" / "data" / "products.json"
        with open(db_path, "r") as file:
            products = json.load(file)

        if id >= len(products):
            return None

        return Product(
            **products[id]
        )

    def get_all(self) -> List[Product]:
        db_path = Path.cwd() / "app" / "db" / "data" / "products.json"
        with open(db_path, "r") as file:
            products = json.load(file)

        return [Product(**product) for product in products]
