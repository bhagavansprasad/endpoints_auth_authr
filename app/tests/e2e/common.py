import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as file:
        data = json.load(file)
        return data['server_url'], data['username'], data['password']
    
    return None, None, None
    
