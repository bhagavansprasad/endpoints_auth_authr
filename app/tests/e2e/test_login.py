import requests
import pytest

def send_login_request(server_url, username, password):
    url = f"{server_url}/login"
    payload = {'username': username,'password': password}
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    return requests.post(url, data=payload, headers=headers)

def process_test_case(server_url, test_case):
    print(f"username :{test_case['username']}")
    print(f"password :{test_case['password']}")
    response = send_login_request(server_url, test_case['username'], test_case['password'])
    print(f"response code :{response.status_code}")
    print(f"response :{response.json()}")
    return response

def parse_response(response):
    retcode = response.status_code
    resp_body = response.json()
    
    return {"retcode": retcode, "resp_body": resp_body}

def validate_response(retval, exp_retcode):
    assert retval["retcode"] >= exp_retcode and retval["retcode"] < exp_retcode+100

server_url = "http://localhost:8000"
test_data = [
    {
        "description": "Valid credentials", 
        "username": "bhagavansprasad@gmail.com", 
        "password": "bjnjnuh",
        "retcode": 200
    },
    {
        "description": "Invalid password",
        "username": "placeholder",
        "password": "wrongpassword",
        "retcode": 400
    }    
]
@pytest.mark.parametrize("test_case", test_data)
def test_login(test_case):
    response = process_test_case(server_url, test_case)
    retval = parse_response(response)
    validate_response(retval, test_case["retcode"])
