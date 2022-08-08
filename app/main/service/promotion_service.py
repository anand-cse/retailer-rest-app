
from app.main import db
from app.main.model.promotion import Promotion
from typing import Dict, Tuple

from app.main.util.helpers import create_id


def create_promotion(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:

    new_promotion = Promotion(
        id=create_id(prefix="PRM"),
        name=data['name'],
        type=data['type'],
        discount=data['discount'],
        is_active=data["is_active"],
        max_discount=data.get("max_discount"),
        product_id=data['product_id'],
    )
    save_changes(new_promotion)

    return new_promotion.get_dict(), 200


def delete_promotion(promotion_id: str) -> Tuple[Dict, int]:
    Promotion.query.filter(Promotion.id == promotion_id).delete()
    db.session.commit()
    return {"message": f"Promotion deleted: {promotion_id}"}, 200


def get_all_promotions():
    return Promotion.query.all()


def get_all_active_promotions():
    return Promotion.query.filter_by(is_active=True).all()


def get_promotions_for_product(product_id):
    return Promotion.query.filter_by(product=product_id, is_active=True).all()


def save_changes(data: Promotion) -> None:
    db.session.add(data)
    db.session.commit()

