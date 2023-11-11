import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_reponse = requests.get(endpoint, json={"query":"Hello World!"}) # HTTP Request
print(get_reponse.text) # Print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON

# print(get_reponse.json())
print(get_reponse.status_code)