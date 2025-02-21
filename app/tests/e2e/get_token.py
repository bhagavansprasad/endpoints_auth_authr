from login import login
from common import load_config

def get_token():
    server_url, username, password = load_config()
    token = login(server_url, username, password)
    
    if(not token):
        print("Login failed...")
        return None
    
    print(token)

if __name__ == "__main__":
    get_token()
