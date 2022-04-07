import requests

endpoint = 'http://localhost:8000/api/product/1/update/'

data = {
    'title': 'new title from put',
    'base_price': 99.00
}

res = requests.put(endpoint, json=data)

print(res.json())