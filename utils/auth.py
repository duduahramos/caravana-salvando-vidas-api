from flask import request, jsonify
import jwt
from utils.utils import generate_password_hash
from functools import wraps

from app import db


def auth():
    auth = request.authorization

    print("teste")
