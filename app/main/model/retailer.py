from sqlalchemy.orm import relationship

from app.main import db


class Retailer(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "retailer"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    products = relationship("Product", back_populates="retailer")

    def get_dict(self):
        """

        Converts the model to dict
        :return:
        """
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d