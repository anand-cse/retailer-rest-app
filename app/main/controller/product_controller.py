import logging
from typing import Dict, Tuple

from flask import request
from flask_restx import Resource, reqparse

from ..service.product_service import get_all_products, create_product, update_product
from ..util.decorator import token_required
from ..util.dto import ProductDto

api = ProductDto.api
_product = ProductDto.product

parser = reqparse.RequestParser()
parser.add_argument("retailer_id", type=str, help="Retailer ID to search for", location="args")


@api.route('/')
class ProductResource(Resource):
    @api.expect(_product, validate=True)
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new product')
    @token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Product """
        data = request.json
        logging.debug(f"Creating a product by:")
        return create_product(data=data)

    @api.expect(parser)
    @api.doc('list_of_all_products')
    @api.marshal_list_with(_product, envelope='data')
    def get(self):
        """List all products"""
        filters = parser.parse_args()
        logging.debug(f"filters::{filters}")
        return get_all_products(filters=filters)


@api.route('/<product_id>')
class PromotionSingleResource(Resource):
    @api.expect(_product, validate=True)
    @api.response(201, 'Product successfully updated.')
    @api.doc('update product')
    @token_required
    def put(self, product_id):
        """Updates an existing Product """
        changes = request.json
        products = get_all_products(filters={"id": product_id})
        the_product_price = products[0].price
        update_msg, update_status = update_product(product_id=product_id, changes=changes)

        if the_product_price > changes.get("price"):
            # TODO: Send event for product price change
            logging.warning(f"Product Price has been decreased::{product_id}")

        return update_msg, update_status
