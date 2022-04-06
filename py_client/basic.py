import requests
# from rest_framework.test import APIClient


endpoint = 'http://localhost:8000/api/'

response1 = requests.post(endpoint, json={'title': 'my product'},
)


print('echoing back res1:', response1.json())
