from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(45), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
    pokemon = db.relationship("Pokemon", backref='owner', lazy=True)
    
    def __init__(self, user_name, email, password, first_name, last_name):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pokemon_name = db.Column(db.String, nullable = False)
    base_hp = db.Column(db.Integer, nullable = False)
    base_attack = db.Column(db.Integer, nullable = False)
    base_defense = db.Column(db.Integer, nullable = False)
    base_experience = db.Column(db.Integer, nullable = False)
    ability_name = db.Column(db.String, nullable = False)
    front_shiny_sprite = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, pokemon_name, base_hp, base_attack, base_defense, base_experience, ability_name, front_shiny_sprite, user_id):
        self.pokemon_name = pokemon_name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_experience = base_experience
        self.ability_name = ability_name
        self.front_shiny_sprite = front_shiny_sprite
        self.user_id = user_id