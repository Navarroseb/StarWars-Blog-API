from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(250))
    email = db.Column(db.String(250))
    people = db.relationship('Person', secondary='favorites_people', backref='users')
    planets = db.relationship('Planet', secondary='favorites_planets', backref='users')
    

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def get_people(self):
        return list(map(lambda person: person.to_dict(), self.people))
    
    def get_planets(self):
        return list(map(lambda planet: planet.to_dict(), self.planets))
    
    def get_ships(self):
        return list(map(lambda ship: ship.to_dict(), self.ships))

    def to_dict(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email
        }

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
        
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    diameter = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    gravity = db.Column(db.String(250)) 
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    population = db.Column(db.String(250))
    

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population
        }



class FavoritePerson(db.Model):
    __tablename__ = 'favorites_people'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "person_id": self.person_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

