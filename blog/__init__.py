from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('blog.config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from blog.views import index_view, manage_view, blog_view