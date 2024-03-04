import requests
import json
url = 'http://54.226.122.107:8000//orders_pydantic'
headers = {
    'accept': 'application/json'
}
params = {
    'product': 'laptop',
    'units': '1'
}

response = requests.post(url, headers=headers, data=json.dumps(params))

print(response.json())
