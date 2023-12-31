from flask import request

from models.user_model import UserModel
from utils.auth import create_jwt
from utils.utils import password_is_correct
from errors.login_errors import IncorrectPassword
from errors.user_errors import UserNotFound


class LoginService:
    def __init__(self) -> None:
        pass

    def get_user_by_user_name(self, login_schema):
        user_model = UserModel.query.filter_by(user_name=login_schema.get("user_name")).first()

        return user_model

    def login(self, login_schema):
        user_model = self.get_user_by_user_name(login_schema)
        if not user_model:
            raise UserNotFound("Usuário não localizado.")

        if not password_is_correct(request.get_json().get("password"), user_model.password):
            raise IncorrectPassword("Senha incorreta.")

        token = create_jwt(user_model.to_dict())

        dict_token = {
            "jwt_token": token
        }

        return dict_token, 200
