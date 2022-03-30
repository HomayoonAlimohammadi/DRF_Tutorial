import requests


endpoint = 'http://localhost:8000/api/'

response = requests.get(endpoint, json={'message': 'hello there'},
                        params={'user':'pazzo'})

print('echoing back:', response.json())