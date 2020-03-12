from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('blog.config')
db = SQLAlchemy(app)

from blog.views import index_view