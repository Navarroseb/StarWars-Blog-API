from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    favCharacter = db.relationship('favorites_characters', backref='users.id', uselist=False)
    favPlanets = db.relationship('favorites_planets', backref='users.id', uselist=False)
    favStarships = db.relationship('favorites_starships', backref='users.id', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }

    def save(self):
        db.session.add(self)
        db.session.commit()    
    
class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    birth_year = db.Column(db.Integer())
    gender = db.Column(db.String(250))
    height = db.Column(db.Integer())
    characterFav = db.relationship('favorites_characters', backref='characters.id', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()    
    
class Favorites_characters(db.Model):
    __tablename__ = 'favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    Characters_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "Characters_id": self.Characters_id,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    planetsFav = db.relationship('favorites_planets', backref='planets.id', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()    
    
class Favorites_planets(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    Planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "Planets_id": self.Planets_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
       
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    passengers_capacity = db.Column(db.Integer)
    pilots = db.Column(db.String(250))
    starshipFav = db.relationship('favorites_starships', backref='starships.id', uselist=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "passengers_capacity": self.passengers_capacity,
            "pilots": self.pilots,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
class Favorites_starships(db.Model):
    __tablename__ = 'favorites_starships'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    Starships_id = db.Column(db.Integer, db.ForeignKey("starships.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "Starships_id": self.Starships_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()