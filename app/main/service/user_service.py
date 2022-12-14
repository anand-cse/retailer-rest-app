import logging
import uuid
import datetime

from app.main import db
from app.main.model.user import User
from typing import Dict, Tuple

from app.main.util.helpers import create_id


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            new_user = User(
                id=create_id(prefix="USR"),
                email=data['email'],
                password=data['password'],
            )
            save_changes(new_user)
            return generate_token(new_user)
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409
    except Exception as e:
        logging.error(f"Error in saving new user::{e}", exc_info=True)
        return "Error in saving new user", 500


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception as e:
        logging.error(f"Error generating token::{e}", exc_info=True)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()

