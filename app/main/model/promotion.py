import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.main import db


class PromotionType(str, enum.Enum):
    FLAT = "FLAT"
    PERCENTAGE = "PERCENTAGE"


class Promotion(db.Model):
    """ Promotion Model for storing promotion related details """
    __tablename__ = "promotion"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum(PromotionType), nullable=False)
    discount = db.Column(db.Float(), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    max_discount = db.Column(db.Float())    # None means infinite
    product_id = db.Column(db.String(50), ForeignKey('product.id'), nullable=False)

    product = relationship("Product", back_populates="promotions")

    def get_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d
