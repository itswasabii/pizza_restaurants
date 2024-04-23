from app.models import Restaurant, Pizza, RestaurantPizza , db

def seed_database():
    # Create and add restaurants
    pizza_house = Restaurant(name='Pizza House', address='123 Main Street')
    cheesy_pizza = Restaurant(name='Cheesy Pizza', address='456 Oak Avenue')
    db.session.add(pizza_house)
    db.session.add(cheesy_pizza)

    # Create and add pizzas
    margherita = Pizza(name='Margherita', ingredients='Tomato sauce, mozzarella cheese, basil')
    pepperoni = Pizza(name='Pepperoni', ingredients='Tomato sauce, mozzarella cheese, pepperoni slices')
    veggie_lovers = Pizza(name='Veggie Lovers', ingredients='Tomato sauce, mozzarella cheese, bell peppers, onions, olives')
    db.session.add(margherita)
    db.session.add(pepperoni)
    db.session.add(veggie_lovers)

    # Create and add restaurant-pizza relationships with prices
    pizza_house_margherita = RestaurantPizza(restaurant_id=pizza_house.id, pizza_id=margherita.id, price=12.99)
    pizza_house_pepperoni = RestaurantPizza(restaurant_id=pizza_house.id, pizza_id=pepperoni.id, price=14.99)
    cheesy_pizza_pepperoni = RestaurantPizza(restaurant_id=cheesy_pizza.id, pizza_id=pepperoni.id, price=15.99)
    cheesy_pizza_veggie_lovers = RestaurantPizza(restaurant_id=cheesy_pizza.id, pizza_id=veggie_lovers.id, price=16.99)
    db.session.add(pizza_house_margherita)
    db.session.add(pizza_house_pepperoni)
    db.session.add(cheesy_pizza_pepperoni)
    db.session.add(cheesy_pizza_veggie_lovers)

    # Commit changes to the database
    db.session.commit()

if __name__ == '__main__':
    seed_database()
