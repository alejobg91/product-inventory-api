# Product Inventory API

API for managing generic products and their attributes.

Product Inventory API

A REST API built with Python and FastAPI to manage a product inventory.

Features

Check API health status.

Retrieve all products.

Retrieve a product by ID.

Create new products.

Update existing products.

Delete products.

Handle errors when a product is not found.

Automated tests using pytest and FastAPI TestClient.

Technologies

Python

FastAPI

Pydantic

Uvicorn

Pytest

Installation

Clone the repository:

git clone https://github.com/alejobg91/product-inventory-api.git

Enter the project directory:

cd product-inventory-api

Install dependencies:

python -m pip install -r requirements.txt

Run the API

python -m uvicorn main:app --reload

Open http://127.0.0.1:8000/docs to explore and test the endpoints using Swagger UI.

Run automated tests

python -m pytest -v

Note

Products are stored in memory. Data resets when the API restarts.

Author

Alejandro Betancourt