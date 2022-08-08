from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.retailer_controller import api as retailer_ns
from .main.controller.product_controller import api as product_ns
from .main.controller.promotion_controller import api as promotion_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


api = Api(
    blueprint,
    title='REST ENDPOINTS WITH JWT AUTH',
    version='1.0',
    description='Assignment submission for Anakin',
    authorizations=authorizations,
    security='apiKey'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(retailer_ns, path='/retailer')
api.add_namespace(product_ns, path='/product')
api.add_namespace(promotion_ns, path='/promotion')
