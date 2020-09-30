import os
from pathlib import Path

from dotenv import load_dotenv

basedir = Path(__file__).parent
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # sql_alchemy_config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email_config
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['aganek9611@gmail.com']

    POSTS_PER_PAGE = 5

    LANGUAGES = ['en', 'ru']
    # BABEL_TRANSLATION_DIRECTORIES = os.path.join(basedir, os.environ.get('BABEL_TRANSLATION_DIRECTORIES'))
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')