# run.py

import sys
sys.path.append('/root/Development/code/4/pizza_restaurants') 
from flask_cors import CORS

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)