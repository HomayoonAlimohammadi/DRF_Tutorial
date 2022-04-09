import requests
from authenticate import authenticate


token = authenticate()
headers = {
    'Authorization': f'Token {token}'
}

endpoint = 'http://localhost:8000/api/product/'

data = {
    'title': 'New Product',
    'base_price': 2.00,
    'discount': 0.4
}

res = requests.post(
    endpoint,
    json=data,
    headers=headers
)

print(res.json())