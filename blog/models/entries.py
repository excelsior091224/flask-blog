from blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, name=None, title=None, text=None):
        self.name = name
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} name:{} title:{} text:{}>'.format(self.id, self.name, self.title, self.text)