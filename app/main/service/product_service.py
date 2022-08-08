from sqlalchemy import select, or_

from app.main import db
from app.main.model.product import Product
from typing import Dict, Tuple

from app.main.model.promotion import Promotion
from app.main.util.helpers import create_id


def create_product(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_product = Product(
        id=create_id(prefix="PRD"),
        name=data['name'],
        retailer_id=data['retailer_id'],
        price=data['price']
    )
    save_changes(new_product)

    return new_product.get_dict(), 200


def get_all_products(filters=None):
    """

    :param filters:
    :return:
    """
    if filters is None:
        filters = {}

    q = db.session.query(Product).outerjoin(Promotion).filter(
        or_(Promotion.is_active == True, Promotion.id.is_(None)))
    for attr, value in filters.items():
        if not value:
            value = ""
        q = q.filter(getattr(Product, attr).like("%%%s%%" % value))
    result = q.all()
    print(f"Result::{result}")
    return result


def update_product(product_id: str, changes: Dict):
    """

    :param product_id:
    :param changes:
    :return:
    """
    Product.query.filter_by(id=product_id).update(changes)
    db.session.commit()
    print("Success fully updated product")
    return {"message": "Product Updated"}, 201


def get_a_product(id):
    return Product.query.filter_by(id=id).first()


def save_changes(data: Product) -> None:
    db.session.add(data)
    db.session.commit()


if __name__ == '__main__':
    create_product(data={
        "name": "",
        "retailer_id": "",
        "price": 20
    })
