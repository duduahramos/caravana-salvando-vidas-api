import string
import random


random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = "".join(random.choice(random_str) for i in range(12))

SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/caravana_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "429af07e-84b3-45e3-8037-6146594a2a37"