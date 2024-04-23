from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
# Initialize SQLAlchemy object
db = SQLAlchemy()

def create_app():
    # Create Flask application instance
    app = Flask(__name__)
    
    CORS(app)
    # Load configuration from Config class
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
   
    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import models within the app context
    with app.app_context():
        from app.models import Restaurant
        
        # Create tables if they don't exist
        db.create_all()

        # Check if Restaurant table is empty
        if not db.session.query(Restaurant).first():
            restaurant1 = Restaurant(name='Dominion Pizza', address='Pizza Inn, Mbagathi, Kenyatta')
            restaurant2 = Restaurant(name='Pizza Hut', address='Prestige, Big Road, Ksm 100')
            db.session.add(restaurant1)
            db.session.add(restaurant2)
            db.session.commit()

    # Import and register routes blueprint
    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
