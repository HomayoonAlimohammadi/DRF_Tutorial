import requests

endpoint = 'http://localhost:8000/api/product/'

res = requests.get(endpoint)

print(res.json())