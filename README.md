# Store REST API

An interesting REST API built with Flask that allows users to manage stores and their items. This API provides endpoints to create and retrieve stores, as well as add and view items within each store. The project includes JSON-based interactions that are ready to be tested using tools like Insomnia or Postman.

## Features

- **Retrieve all stores**: View all existing stores with their items.
- **Create a new store**: Add a new store with a unique name.
- **Add items to a store**: Add items, such as products with a name and price, to a specified store.
- **View a specific store**: Retrieve details of a specific store by its name.
- **View a specific item**: Retrieve details of a specific item within a store.

## Tech Stack

- **Python**: Primary programming language
- **Flask**: Micro-framework for handling requests and creating RESTful API endpoints
- **Insomnia**: For testing API endpoints (Insomnia export included)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chriswilder3/Store-REST-API.git
    cd Store-REST-API
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    export FLASK_APP=app.py  # Adjust if your file has a different name
    export FLASK_ENV=development
    flask run
    ```

    The app will run on `127.0.0.1:5000` by default.

## API Documentation

### Endpoints

- **GET** `/store`
  - Retrieves all stores with their items.
  - **Response**: `{ "stores": [...] }`

- **POST** `/store`
  - Creates a new store.
  - **Request Body**: `{ "name": "My Store", "items": [] }`
  - **Response**: `{ "name": "My Store", "items": [] }`

- **POST** `/store/<string:name>/item`
  - Adds a new item to the specified store.
  - **Request Body**: `{ "name": "table", "price": 5000 }`
  - **Response**: `{ "name": "table", "price": 5000 }`

- **GET** `/store/<string:name>`
  - Retrieves details of a specific store.
  - **Response**: `{ "name": "My Store", "items": [...] }`

- **GET** `/store/<string:storename>/<string:itemname>`
  - Retrieves details of a specific item within a store.
  - **Response**: `{ "name": "table", "price": 5000 }`

### Example Insomnia Collection

For testing, an Insomnia collection is included in the project. You can import it directly into Insomnia to access all configured endpoints.

## Testing

You can test the API endpoints manually with Insomnia, Postman, or by using cURL commands. A sample Insomnia export file is included for quick setup.

## Future Enhancements

- Implement authentication to restrict access to certain endpoints.
- Add data persistence using a database like SQLite or MongoDB.
- Expand error handling and data validation for more robust API interactions.

## Contributing

Feel free to open issues and submit pull requests if you'd like to contribute to the project. All contributions are welcome!

