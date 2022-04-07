import requests

endpoint = 'http://localhost:8000/api/product/2394/'

res = requests.get(endpoint)

print(res.json())