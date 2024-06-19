import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_addition():
    response = client.post("/api/v1/add", json={"batched": "id0101", "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["batched"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data

def test_addition_empty():
    response = client.post("/api/v1/add", json={"batched": "id0102", "payload": []})
    assert response.status_code == 200
    data = response.json()
    assert data["batched"] == "id0102"
    assert data["response"] == []
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data

def test_addition_invalid_input():
    response = client.post("/api/v1/add", json={"batched": "id0103", "payload": "not_a_list"})
    assert response.status_code == 422
