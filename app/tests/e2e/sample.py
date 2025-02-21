import requests

def send_login_request():
    url = "http://localhost:8000/login"

    payload = {
        'username': 'bhagavansprasad@gmail.com',
        'password': 'bjnjnuh'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)

    print("Response Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except Exception as e:
        print("Failed to parse response as JSON.", str(e))

if __name__ == "__main__":
    send_login_request()
