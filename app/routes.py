# app/routes.py

from flask import Blueprint, jsonify, request
from app.models import Restaurant, Pizza, RestaurantPizza, db

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def index():
    return 'Welcome to Pizza Restaurant API!'

@routes_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.serialize() for restaurant in restaurants])

@routes_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        return jsonify(restaurant.serialize_with_pizzas())
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@routes_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        # Delete the restaurant
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204  
    else:
        return jsonify({'error': 'Restaurant not found'}), 404


@routes_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.serialize() for pizza in pizzas])

@routes_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price and pizza_id and restaurant_id:
        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(Pizza.query.get(pizza_id).serialize())
    else:
        return jsonify({'errors': ['validation errors']}), 400
