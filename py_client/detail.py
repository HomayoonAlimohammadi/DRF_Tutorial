import requests

endpoint = 'http://localhost:8000/api/product/9/'

res = requests.get(endpoint)

print(res.json())