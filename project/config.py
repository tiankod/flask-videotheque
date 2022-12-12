"""Flask configuration."""
from os import environ
from dotenv import load_dotenv

# valeurs par defaut
environ.setdefault('SESSION_COOKIE_HTTPONLY', "true")

# var env dans fichier .env
load_dotenv()
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
SESSION_COOKIE_HTTPONLY = environ.get('SESSION_COOKIE_HTTPONLY')
REMEMBER_COOKIE_HTTPONLY = environ.get('REMEMBER_COOKIE_HTTPONLY')
