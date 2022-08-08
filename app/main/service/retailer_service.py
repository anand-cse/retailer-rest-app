import uuid
import datetime

from app.main import db
from app.main.model.retailer import Retailer
from typing import Dict, Tuple

from app.main.util.helpers import create_id


def create_retailer(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_retailer = Retailer(
        id=create_id(prefix="RTL"),
        name=data['name'],
    )
    save_changes(new_retailer)
    return new_retailer.get_dict(), 200


def get_all_retailers():
    return Retailer.query.all()


def get_a_retailer(id):
    return Retailer.query.filter_by(id=id).first()


def save_changes(data: Retailer) -> None:
    db.session.add(data)
    db.session.commit()

