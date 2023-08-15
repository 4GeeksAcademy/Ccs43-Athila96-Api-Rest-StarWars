from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    favorite_planet = db.relationship("FavoritePlanet", backref="user")
    favorite_peoples = db.relationship("FavoritePeople", backref="user")

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    created = db.Column(db.String(250), unique=False, nullable=False)
    diameter = db.Column(db.String(250), unique=False, nullable=False)
    edited = db.Column(db.String(250), unique=False, nullable=False)
    gravity = db.Column(db.String(250), unique=False, nullable=False)
    orbital_period = db.Column(db.String(250), unique=False, nullable=False)
    population = db.Column(db.String(250), unique=False, nullable=False)
    rotation_period = db.Column(db.String(250), unique=False, nullable=False)
    surface_water = db.Column(db.String(250), unique=False, nullable=False)
    terrain = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(500), unique=False, nullable=False)
    favorite_planets = db.relationship("FavoritePlanet",backref="planets")

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created,
            "diameter": self.diameter,
            "edited": self.edited,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
            #"favorite_planets": self.favorite_planets


            # do not serialize the password, its a security breach
        }
    
class Peoples(db.Model):
    __tablename__ = "peoples"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    eyes_color = db.Column(db.String(250), unique=False, nullable=False)
    films = db.Column(db.String(250), unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    height = db.Column(db.String(250), unique=False, nullable=False)
    homeworld = db.Column(db.String(250), unique=False, nullable=False)
    mass = db.Column(db.String(250), unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)
    created = db.Column(db.String(250), unique=False, nullable=False)
    species = db.Column(db.String(250), unique=False, nullable=False)
    starships = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(500), unique=False, nullable=False)
    vehicles = db.Column(db.String(250), unique=False, nullable=False)
    favorite_peoples = db.relationship("FavoritePeople", backref="peoples")

    def __repr__(self):
        return '<Peoples %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eyes_color": self.eyes_color,
            "films": self.films,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "created": self.created,
            "species": self.species,
            "starships": self.starships,
            "url": self.url,
            "vehicles": self.vehicles,
        
            # do not serialize the password, its a security breach
        }

class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))

    def __repr__(self):
        return '<FavoritePlanet %r>' % self.id
    
    def serialize(self):
        return {
           # "id": self.id,
           # "user_id": self.user_id,
            "planet": self.planets.serialize()
        }

class FavoritePeople(db.Model):
    __tablename__ = "favorite_people"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    people_id = db.Column(db.Integer, db.ForeignKey("peoples.id"))

    def __repr__(self):
        return '<FavoritePeoples %r>' % self.id
    
    def serialize(self):
        return {
            #"id": self.id,
            #"user_id": self.user_id,
            #"people_id": self.people_id
            "character": self.peoples.serialize()
        }

