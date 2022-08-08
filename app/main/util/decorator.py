import logging
from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from typing import Callable


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')
        print(f"token::{data}, {status}")
        if not token:
            return data, status

        request.user_id = token.get("user_id")
        return f(*args, **kwargs)

    return decorated
