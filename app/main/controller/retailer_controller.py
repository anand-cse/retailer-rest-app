import logging
from typing import Dict, Tuple

from flask import request
from flask_restx import Resource

from ..service.retailer_service import get_all_retailers, create_retailer
from ..util.decorator import token_required
from ..util.dto import RetailerDto

api = RetailerDto.api
_retailer = RetailerDto.retailer


@api.route('/')
class RetailerResource(Resource):
    @api.expect(_retailer, validate=True)
    @api.response(201, 'Retailer successfully created.')
    @api.doc('create a new retailer')
    @api.doc(security="apiKey")
    @token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Retailer """
        data = request.json
        logging.debug(f"Creating a retailer by::{request.user_id}")
        return create_retailer(data=data)

    @api.doc('list_of_all_retailers')
    @api.marshal_list_with(_retailer, envelope='data')
    def get(self):
        """List all retailers"""
        return get_all_retailers()



