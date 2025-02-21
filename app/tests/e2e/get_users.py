from login import login
from common import load_config
import requests

def send_get_users_request(url, token):
    """Send a GET request to fetch users."""
    full_url = f"{url}/users"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(full_url, headers=headers)
    return response

def get_users():
    server_url, username, password = load_config()
    token = login(server_url, username, password)
    
    if(not token):
        print("Login failed...")
        return None
    
    response = send_get_users_request(server_url, token)
    print(f"Response Status Code: {response.status_code}")
    data = response.json()
    print(data)

if __name__ == "__main__":
    get_users()
