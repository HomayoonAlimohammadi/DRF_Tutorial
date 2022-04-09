from getpass import getpass
import requests

def authenticate():

    username = input('Username: ')
    password = getpass()

    auth_endpoint = 'http://localhost:8000/api/auth/'
    credentials = {
        'username': username,
        'password': password
    }

    auth_res = requests.post(auth_endpoint, json=credentials)
    print(auth_res.status_code)
    print(auth_res.json())
    if auth_res.status_code == 200:
        return auth_res.json().get('token')

    return {'detail': 'Invalid credentials.'}
