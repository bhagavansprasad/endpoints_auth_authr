import requests
import json
import os
from common import load_config

def send_login_request(server_url, username, password):
    """Send a login request to the server."""
    url = f"{server_url}/login"
    payload = {
        'username': username,
        'password': password
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=payload, headers=headers)

def execute_test_case(server_url, test_case):
    """Execute a single test case and print the result."""
    print(f"Running test case: {test_case['description']}")
    response = send_login_request(server_url, test_case['username'], test_case['password'])

    print(f"Response Status Code: {response.status_code}")
    try:
        reply = response.json()
        print(f"Response Body: {reply}")
    except json.JSONDecodeError:
        print("Response Body: Not a valid JSON")
        
    return response

def generate_test_cases(username, correct_password):
    """Generate test cases for a given user."""
    return [
        {"description": "Valid credentials", "username": username, "password": correct_password},
        # {"description": "Invalid password", "username": username, "password": "wrongpassword"},
        # {"description": "Missing username", "username": "", "password": correct_password},
        # {"description": "Missing password", "username": username, "password": ""},
        # {"description": "Invalid username", "username": "wronguser@gmail.com", "password": correct_password},
    ]

def test_user_login(server_url, username, password):
    """Run all test cases for a single user."""
    print(f"Testing for user: {username}")

    test_cases = generate_test_cases(username, password)
    for test_case in test_cases:
        execute_test_case(server_url, test_case)
        print("-" * 50)

def run_tests():
    """Run tests for all users defined in the configuration."""
    server_url, username, password = load_config()
    test_user_login(server_url, username, password)

def login(url, username, password):
    response = send_login_request(url, username, password)
    
    if response.status_code != 200:
        print(response.json())
        return None

    reply = response.json()
    if "access_token" in reply:
        return reply['access_token']

    return None        

if __name__ == "__main__":
    run_tests()
