import string
import random


random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = "".join(random.choice(random_str) for i in range(12))

SQLALCHEMY_DATABASE_URI = "mysql://root@127.0.0.1:3306/caravana_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY_PASSWORD = "429af07e-84b3-45e3-8037-6146594a2a37"
SECRET_KEY_JWT = "93713a24-4a7c-4957-9717-47098af90f39"
SECRET_KEY_SESSION = "91f5c636-c0a8-4a18-aecf-568cd4a23681"
