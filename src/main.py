"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import Person
from models import Planet

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda ship: ship.to_dict(), users))
    return jsonify(users), 200

@app.route("/users/<int:user_id>/favorites", methods=['GET'])
def get_user_favorites(user_id):
    user = Users.query.get(user_id)
    people = users.get_people()
    planets = users.get_planets()
    
    return jsonify({
        "people": people,
        "planets": planets,
    }), 200

@app.route("/users", methods=['POST'])
def create_user():
    user = User()
    user.email = request.json.get('email')
    user.password = request.json.get('password')
    user.save()
    
    return jsonify(user.to_dict()), 201

@app.route("/users/<int:user_id>/favorites_planets", methods=['POST'])
def create_favorite_planet(user_id):
    favorite_planet = FavoritePlanet()
    favorite_planet.user_id = user_id
    favorite_planet.planet_id = request.json.get('planet_id')
    favorite_planet.save()
    
    return jsonify(favorite_planet.to_dict()), 201

@app.route("/users/<int:user_id>/favorites_people/<int:favorite_person_id>", methods=['DELETE'])
def delete_favorite_person(user_id, favorite_person_id):
    favorite_person = FavoritePerson.query.get(favorite_person_id)
    favorite_person.delete()

    return jsonify(favorite_person.to_dict()), 201

@app.route("/users/<int:user_id>/favorites_planets/<int:favorite_planet_id>", methods=['DELETE'])
def delete_favorite_planet(user_id, favorite_planet_id):
    favorite_planet = FavoritePlanet.query.get(favorite_planet_id)
    favorite_planet.delete()

    return jsonify(favorite_planet.to_dict()), 201



@app.route("/people", methods=['GET'])
def getPeople():
    people = Person.query.all()
    people = list(map(lambda person: person.to_dict(), people))
    return jsonify(people), 200

@app.route("/people/<int:person_id>", methods = ["GET"])
def getPerson(person_id):
    person = Person.query.get(person_id)
    
    if person:
        return jsonify(person.to_dict())

    return jsonify({"message": "Person not found"})

@app.route("/users/<int:user_id>/favorites_people", methods=['POST'])
def create_favorite_person(user_id):
    favorite_person = FavoritePerson()
    favorite_person.user_id = user_id
    favorite_person.person_id = request.json.get('person_id')
    favorite_person.save()
    
    return jsonify(favorite_person.to_dict()), 201

@app.route("/people", methods=['POST'])
def createPerson():
    person = Person()
    person.name = request.json.get('name')
    person.height = request.json.get('height')
    person.mass = request.json.get('mass')
    person.hair_color = request.json.get('hair_color')
    person.skin_color = request.json.get('skin_color')
    person.eye_color = request.json.get('eye_color')
    person.birth_year = request.json.get('birth_year')
    person.gender = request.json.get('gender')
    person.save()
    
    return jsonify(person.to_dict()), 201



@app.route("/planets", methods=['GET'])
def getPlanets():
    planets = planet.query.all()
    planets = list(map(lambda planet: planet.to_dict(), planets))
    return jsonify(planets), 200

@app.route("/planets/<int:planet_id>", methods = ["GET"])
def getPlanet(planet_id):
    planet = Planet.query.get(planet_id)
    
    if planet:
        return jsonify(planet.to_dict())

    return jsonify({"message": "Planet not found"})

@app.route("/planets", methods=['POST'])
def createPlanet():
    planet = Planet()
    planet.name = request.json.get('name')
    planet.rotation_period = request.json.get('rotation_period')
    planet.orbital_period = request.json.get('orbital_period')
    planet.diameter = request.json.get('diameter')
    planet.climate = request.json.get('climate')
    planet.gravity = request.json.get('gravity')
    planet.terrain = request.json.get('terrain')
    planet.surface_water = request.json.get('surface_water')
    planet.population = request.json.get('population')
    planet.save()
    
    return jsonify(planet.to_dict()), 201


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
