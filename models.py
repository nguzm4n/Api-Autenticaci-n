from flask_sqlalchemy import SQLAlchemy
from math import floor
from datetime import datetime
db = SQLAlchemy()


class User(db.Model):
    """
    Tabla correspondiente a los usuarios
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name":self.name
            
        }

    def save(self):
        db.session.add(self)
        db.session.commit()