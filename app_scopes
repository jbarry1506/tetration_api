# API
from tetpyclient import RestClient
import requests
import urllib3

# FORMATTING
import pprint
import json

# fun fact - scope names can only be 40 characters long
scope_name = "ALL:MY:SCOPES:WILL:LOOK:LIKE:THIS" 
# Tetration Keys
API_SECRET = <shhhh....it's secret>
API_KEY = <Vinz Clortho, Keymaster of Gozer>

# This /app_scopes resource is defined on the OpenAPI documentation
# getting a specific scope
CURRENT_GET_ENDPOINT = '/app_scopes'

# Create the Tetration REST Client 
API_ENDPOINT = 'https://tetbdc.myco.int/openapi/v1'
rc = RestClient(API_ENDPOINT, api_secret=API_SECRET, api_key=API_KEY, verify=False)

resp = rc.get(CURRENT_GET_ENDPOINT)

# make sure we get a good response from the request
if resp.status_code != 200:
   print("Unsuccessful request returned code: {} , \
       response: {}".format(resp.status_code,resp.text))
       
results = resp.json()

sc_checklist = {}
for check in results:
    sc_checklist[check['name']] = {
        "name":check['name'],
        "id":check['id'],
        "dirty":check['dirty']
    }
    
try:
    print(sc_checklist[scope_name]['name'])
    print(sc_checklist[scope_name]['id'])
    print(sc_checklist[scope_name]['dirty'])
except Exception as e:
    print e
    pass

print("the results are in")
