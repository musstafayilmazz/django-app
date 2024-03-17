from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="KgBhilTokcPM4WPjeVaLwrKYJuwZ3T5QOwT6iAWOPZz8nDquOak",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["hhtp://localhost:8080"]
