import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///blog_db.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.environ.get('SECRET_KEY')