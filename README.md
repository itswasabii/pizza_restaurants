# pizza_restaurants


This is a Flask-based API for managing pizza restaurants
## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/itswasabii/pizza_restaurants
    ```

2. Navigate to the project directory:

    ```bash
    cd pizza_restaurants
    ```

3. Install dependencies:

    ```bash
    pipenv install
    ```
      pipenv shell
4. Run the application:

    ```bash
    Flask run
    ```

The application should now be running locally on http://127.0.0.1:5000/.

## Endpoints

The API provides the following endpoints:

- `GET /restaurants`: Get a list of all restaurants.
- `GET /restaurants/<id>`: Get details of a specific restaurant by its ID.
- `DELETE /restaurants/<id>`: Delete a restaurant by its ID.
- `GET /pizzas`: Get a list of all pizzas.
- `POST /restaurant_pizzas`: Create a new association between a restaurant and a pizza.

## Data Validation

The API enforces the following data validation rules:

- Restaurant names must be unique and less than 50 characters in length.
- Restaurant addresses must be provided and can't be empty.
- Restaurant pizzas must have prices between 1 and 30.

## Testing

You can test the API using tools like Postman or cURL. Make sure to send requests to the appropriate endpoints with the required parameters.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.