from blog import db

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hashed_password = db.Column(db.String(100), nullable=False)

    def __init__(self, name=None, hashed_password=None):
        self.name = name
        self.hashed_password = hashed_password
    
    def __repr__(self):
        return '<Account id:{} name:{} hashed_password:{}>'.format(self.id, self.name, self.hashed_password)