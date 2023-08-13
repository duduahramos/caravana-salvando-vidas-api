import hashlib
import uuid

from configs import config


def only_number(value: str) -> str:
    # Remova qualquer caractere não numérico do valor
    value_only_numbers = ''.join(filter(str.isdigit, value))

    return value_only_numbers


def generate_uuid():
    return uuid.uuid4().bytes


def generate_password_hash(password: str) -> str:
    _secret = config.SECRET_KEY

    password_plus_secret = bytes(password + _secret, "ISO8859_1")

    hashed_password = hashlib.md5(password_plus_secret).hexdigest()

    return hashed_password
