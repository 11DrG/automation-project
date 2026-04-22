import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-api-key": API_KEY}

def test_get_users():
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "John", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == "John"

def test_login_successful():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failed():
    payload = {"email": "invalid@reqres.in", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 400

def test_update_user():
    payload = {"name": "John Updated", "job": "Senior QA Engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 204

def test_create_and_fetch_user():
    payload = {"name": "Maria", "job": "QA Engineer"}
    create_response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]
    assert user_id is not None