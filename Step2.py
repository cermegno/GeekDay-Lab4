###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")
print response.content

obj = json.loads(response.content)
print "Timestamp is: ", obj['timestamp']
print "Latitude is: ", obj['iss_position']['latitude']

print type(response.content)
print type(obj)
