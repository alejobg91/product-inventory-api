from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    response = client.post(
    "/products",
    json={"name": "martillo de prueba", "price": 50}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "martillo de prueba"
    assert response.json()["price"] == 50
    assert "id" in response.json()

def test_update_product():
    response = client.put(
        "/products/1",
        json={"name": "madera actualizada", "price": 500}
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "madera actualizada"
    assert response.json()["price"] == 500

def test_delete_product():
    response = client.delete("/products/2")

    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"

def test_product_not_found():
    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"
    
    

