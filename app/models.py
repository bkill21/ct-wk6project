from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe

from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    token = db.Column(db.String(250), unique=True)
    heros = db.relationship('Hero', backref='creator', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def add_token(self):
        setattr(self,'token',token_urlsafe(32))
    
    def get_id(self):
        return str(self.user_id)
    
class Hero(db.Model):
    hero_id = db.Column(db.Integer, primary_key=True)
    hero_name = db.Column(db.String(60))
    power = db.Column(db.String(50))
    hero_lore = db.Column(db.String(500))
    user_id= db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Hero: {self.hero_name}\nPowers: {self.power}\nLore: {self.hero_lore}\nCreator: {self.user_id}\nCreated: {self.creation_date}'