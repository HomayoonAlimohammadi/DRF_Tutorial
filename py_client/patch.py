import requests

endpoint = 'http://localhost:8000/api/product/1/update/'

data = {
    'title': 'new title from patch'
}

res = requests.patch(endpoint, json=data)

print(res.json())