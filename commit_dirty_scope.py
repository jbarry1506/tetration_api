# API
from tetpyclient import RestClient
import requests
import urllib3

# FORMATTING
import pprint
import json

scope_name = "ALL:MY:SCOPES"
# Tetration Keys
API_SECRET = <Can't tell you>
API_KEY = <The key to happiness is helping others>

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
        "dirty":check['dirty'],
        "root":check['root_app_scope_id']
    }

parent_scope = sc_checklist[scope_name]
parent_scope_id = parent_scope["id"]
root_scope_id = parent_scope["root"]
print('parent: ' + parent_scope_id)
print('root: ' + root_scope_id)

# This is the dirty part - hehehe
resp = rc.post("/app_scopes/commit_dirty?root_app_scope_id=" + root_scope_id)
results = resp.json()
print(results)
