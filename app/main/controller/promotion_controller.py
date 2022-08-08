import logging
from typing import Dict, Tuple

from flask import request
from flask_restx import Resource

from ..service.promotion_service import get_all_promotions, create_promotion, delete_promotion
from ..util.decorator import token_required
from ..util.dto import PromotionDto

api = PromotionDto.api
_promotion = PromotionDto.promotion


@api.route('/')
class PromotionResource(Resource):
    @api.expect(_promotion, validate=True)
    @api.response(201, 'Promotion successfully created.')
    @api.doc('create a new promotion')
    @token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Promotion """
        data = request.json
        # logging.debug(f"Creating a promotion by::{request.user_id}")
        return create_promotion(data=data)

    @api.doc('list_of_all_promotions')
    @api.marshal_list_with(_promotion, envelope='data')
    def get(self):
        """List all promotions"""
        return get_all_promotions()


@api.route('/<promotion_id>')
class PromotionSingleResource(Resource):
    @api.response(201, 'Promotion successfully deleted.')
    @api.doc('delete a promotion')
    @token_required
    def delete(self, promotion_id) -> Tuple[Dict[str, str], int]:
        """Deletes an existing Promotion """
        return delete_promotion(promotion_id=promotion_id)




