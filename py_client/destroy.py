import requests

product_id = input('ID of the product to delete: ')

try: 
    product_id = int(product_id)
except ValueError:
    print('invalid product ID')
    product_id = None

if product_id:
    endpoint = f'http://localhost:8000/api/product/{product_id}/destroy/'
    res = requests.delete(endpoint)

    print(res.status_code)