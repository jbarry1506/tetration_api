# API
from tetpyclient import RestClient
import requests
import urllib3

# FORMATTING
import pprint
import json

# Tetration Keys
API_SECRET = <secret agent man>
API_KEY = <friends don't let friends do key-to> #wahwah lol

# This /app_scopes resource is defined on the OpenAPI documentation
# getting a specific scope
CURRENT_GET_ENDPOINT = '/applications'

# Create the Tetration REST Client 
API_ENDPOINT = 'https://tetbdc.myco.int/openapi/v1'
rc = RestClient(API_ENDPOINT, api_secret=API_SECRET, api_key=API_KEY, verify=False)

resp = rc.get(CURRENT_GET_ENDPOINT)

# make sure we get a good response from the request
if resp.status_code != 200:
   print("Unsuccessful request returned code: {} , \
       response: {}".format(resp.status_code,resp.text))
results = resp.json()

pprint.pprint(results[0])
