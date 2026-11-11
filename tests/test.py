
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Test 1: Home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200


# Test 2: Health endpoint
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# Test 3: Addition
def test_addition():
    response = client.post("/calculate", json={
        "num1": 20,
        "num2": 10,
        "operation": "add"
    })

    assert response.status_code == 200
    assert response.json()["result"] == 30


# Test 4: Subtraction
def test_subtraction():
    response = client.post("/calculate", json={
        "num1": 50,
        "num2": 20,
        "operation": "subtract"
    })

    assert response.status_code == 200
    assert response.json()["result"] == 30


# Test 5: Multiplication
def test_multiplication():
    response = client.post("/calculate", json={
        "num1": 5,
        "num2": 4,
        "operation": "multiply"
    })

    assert response.status_code == 200
    assert response.json()["result"] == 20


# Test 6: Division
def test_division():
    response = client.post("/calculate", json={
        "num1": 100,
        "num2": 5,
        "operation": "divide"
    })

    assert response.status_code == 200
    assert response.json()["result"] == 20


# Test 7: Division by zero
def test_division_by_zero():
    response = client.post("/calculate", json={
        "num1": 10,
        "num2": 0,
        "operation": "divide"
    })

    assert response.status_code == 400


# Test 8: Invalid operation
def test_invalid_operation():
    response = client.post("/calculate", json={
        "num1": 10,
        "num2": 5,
        "operation": "power"
    })

    assert response.status_code == 400


# Test 9: Decimal calculation
def test_decimal_addition():
    response = client.post("/calculate", json={
        "num1": 10.5,
        "num2": 5.5,
        "operation": "add"
    })

    assert response.status_code == 200
    assert response.json()["result"] == 16.0


# Test 10: Missing input
def test_missing_input():
    response = client.post("/calculate", json={
        "num1": 10,
        "operation": "add"
    })

    assert response.status_code == 422
