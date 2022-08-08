from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.main import db


class Product(db.Model):
    """ Product Model for storing product related details """
    __tablename__ = "product"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float(), nullable=False)
    retailer_id = db.Column(db.String(50), ForeignKey('retailer.id'), nullable=False)

    retailer = relationship("Retailer", back_populates="products")
    promotions = relationship("Promotion", back_populates="product")

    def get_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d



