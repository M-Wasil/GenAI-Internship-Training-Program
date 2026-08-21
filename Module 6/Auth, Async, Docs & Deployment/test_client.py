import requests
import json

BASE_URL = "http://localhost:8000"  # Change to your deployed URL

# 1. Register a user
print("1. Registering user...")
register_data = {
    "email": "test@example.com",
    "username": "testuser",
    "full_name": "Test User",
    "age": 25,
    "password": "securepassword123"
}
response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=register_data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 2. Get access token
print("2. Getting access token...")
login_data = {
    "username": "test@example.com",  # OAuth2 expects 'username' field
    "password": "securepassword123"
}
response = requests.post(f"{BASE_URL}/api/v1/auth/token", data=login_data)  # Note: data, not json
print(f"Status: {response.status_code}")
token_data = response.json()
print(f"Token: {token_data}\n")

# 3. Get current user info
print("3. Getting current user...")
headers = {"Authorization": f"Bearer {token_data['access_token']}"}
response = requests.get(f"{BASE_URL}/api/v1/auth/me", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 4. Create a new user (requires auth)
print("4. Creating a new user (requires auth)...")
new_user = {
    "email": "john@example.com",
    "username": "john_doe",
    "full_name": "John Doe",
    "age": 30,
    "password": "anotherpass123"
}
response = requests.post(f"{BASE_URL}/api/v1/users/", json=new_user, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 5. Get all users
print("5. Getting all users...")
response = requests.get(f"{BASE_URL}/api/v1/users/", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")
