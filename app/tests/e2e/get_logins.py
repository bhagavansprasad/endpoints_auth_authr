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

def get_logins():
    server_url, username, password = load_config()
    token = login(server_url, username, password)
    
    if(not token):
        print("Login failed...")
        return None
    
    response = send_get_users_request(server_url, token)
    print(f"Response Status Code: {response.status_code}\n")
    data = response.json()
    tlist = []
    
    for d in data:
        tlist.append({'user_e_mail_id': d['user_e_mail_id'], 'user_password': d['user_password']})

    for d in tlist:
        print(d)
        

if __name__ == "__main__":
    get_logins()
