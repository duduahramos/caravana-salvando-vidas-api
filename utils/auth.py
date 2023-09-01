from functools import wraps
import jwt
from flask import request
import json
import cryptocode

from models.user_model import UserModel
from utils.utils import generate_password_hash
from configs.config import SECRET_KEY_JWT, SECRET_KEY_SESSION


def create_jwt(user_dict):
    print(user_dict)

    session_dict = {
        "id": user_dict.get("id"),
        "user_name": user_dict.get("user_name"),
        "admin": user_dict.get("admin")
    }

    session_str = json.dumps(session_dict)
    session_encrypt_str = cryptocode.encrypt(session_str, SECRET_KEY_SESSION)
    token = jwt.encode({"session": session_encrypt_str}, SECRET_KEY_JWT, algorithm="HS256")

    return token


def token_required(function_decorated):
    @wraps(function_decorated)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return [{"message": "Token vazio."}, 401]

        try:
            token_decoded = jwt.decode(token, SECRET_KEY_JWT, algorithms="HS256")
            # session_dict = json.loads(cryptocode.decrypt(token_decoded["session"], SECRET_KEY_SESSION))
            # current_user = UserModel.query.filter_by(user_name=session_dict.get("user_name")).first()

            # chama a funcao que recebeu o decorator e inicializa ela com os argumentos
            # recebidos na decorated
            return function_decorated(*args, **kwargs)
        except Exception as e:
            print(e.args)

            return [{"message": "Token inválido ou expirado."}, 401]
    return decorated
