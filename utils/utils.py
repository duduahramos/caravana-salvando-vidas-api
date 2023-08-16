from flask import request
import hashlib
import uuid
import json
import cryptocode
import jwt

from configs.config import SECRET_KEY_JWT, SECRET_KEY_SESSION, SECRET_KEY_PASSWORD


def only_number(value: str) -> str:
    # Remova qualquer caractere não numérico do valor
    value_only_numbers = ''.join(filter(str.isdigit, value))

    return value_only_numbers


def generate_uuid():
    return uuid.uuid4().bytes


def generate_password_hash(password: str) -> str:
    password_plus_secret = bytes((password + SECRET_KEY_PASSWORD), "ISO8859_1")

    hashed_password = hashlib.md5(password_plus_secret).hexdigest()

    return hashed_password


def password_is_correct(senha_request, senha_bd) -> bool:
    senha_request_hash = generate_password_hash(senha_request)

    if senha_request_hash == senha_bd:
        return True
    else:
        return False

