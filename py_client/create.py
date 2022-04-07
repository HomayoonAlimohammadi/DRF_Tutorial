import requests

endpoint = 'http://localhost:8000/api/product/'

data = {
    'title': 'New Product',
    'base_price': 2.00,
    'discount': 0.4
}

res = requests.post(endpoint, json=data)

print(res.json())