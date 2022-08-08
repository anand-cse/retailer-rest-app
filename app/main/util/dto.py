from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user\'s password'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class RetailerDto:
    api = Namespace('retailer', description='retailer related operations')
    retailer = api.model('retailer', {
        'id': fields.String(readonly=True, description='The ID of retailer'),
        'name': fields.String(required=True, description='The name of retailer'),
    })


class PromotionDto:
    api = Namespace('promotion', description='promotion related operations')
    promotion = api.model('promotion', {
        'id': fields.String(readonly=True, description='The ID of the promotion'),
        'name': fields.String(required=True, description='The name of promotion'),
        'discount': fields.Float(required=True, description='The name of brand'),
        'type': fields.String(required=True, description='The name of brand', enum=["FLAT", "PERCENTAGE"]),
        'is_active': fields.Boolean(required=True, description='The name of brand'),
        'max_discount': fields.Float(required=True, description='The name of brand'),
        'product_id': fields.String(required=True, description='The Retailer ID of the product'),
    })


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'id': fields.String(readonly=True, description='The ID of the product'),
        'name': fields.String(required=True, description='The name of product'),
        'price': fields.Float(required=True, description='The name of brand'),
        'retailer_id': fields.String(required=True, description='The Retailer ID of the product'),
        'promotions': fields.List(readonly=True, cls_or_instance=fields.Nested(PromotionDto.promotion),
                                  description="True")
    })
