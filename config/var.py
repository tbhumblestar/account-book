import environ
from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


def required(key, default_value=None):
    try:
        value = env(key)
    except:
        if not default_value:
            raise ImproperlyConfigured(f"Set the {key} environment variable")
        value = default_value
    return value


var = {
    "db": {
        "secret_key": required("DB_SECRET"),
        "name": required("DB_NAME"),
        "user": required("DB_USER"),
        "host": required("DB_HOST"),
        "port": required("DB_PORT"),
    },
    "jwt": {
        "secret": required("JWT_SECRET"),
        "expired_days": required("JWT_EXPIRED_DAYS", 3),
    },
    "cors": {
        "domain": required("CORS_DOMAIN"),
    },
}
