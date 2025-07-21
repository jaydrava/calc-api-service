from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


def test_calculate_add():
    response = client.post(
        "/calculate", json={"operand1": 10, "operand2": 5, "operation": "add"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_calculate_divide_by_zero():
    response = client.post(
        "/calculate", json={"operand1": 10, "operand2": 0, "operation": "divide"}
    )
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]


def test_calculate_invalid_operation():
    response = client.post(
        "/calculate", json={"operand1": 10, "operand2": 5, "operation": "modulus"}
    )
    assert response.status_code == 422  # validation error from Pydantic schema
