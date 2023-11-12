import json
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_reponse = requests.get(endpoint, params={"product_id": 123}) # HTTP Request
# print(get_reponse.text) # Print raw text response
# print(get_reponse.status_code)


# HTTP Request -> HTML
# REST API HTTP Request -> JSON

print(get_reponse.json())
# print(get_reponse.status_code)