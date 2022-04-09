import requests
from authenticate import authenticate


token = authenticate()
headers = {
    'Authorization': f'Token {token}'
}

endpoint = 'http://localhost:8000/api/product/1/update/'

data = {
    'title': 'new title from put',
    'base_price': 99.00
}

res = requests.put(endpoint, json=data, headers=headers)

print(res.json())