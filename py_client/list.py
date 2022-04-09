import requests
from authenticate import authenticate


token = authenticate()
headers = {
    'Authorization': f'Token {token}'
}

endpoint = 'http://localhost:8000/api/product/'

res = requests.get(endpoint, headers=headers)

print(res.json())