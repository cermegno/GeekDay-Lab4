###########################################################
## Sometimes API - GET requests require passing parameters
## When will it pass through Bangkok? What are the coordinates?
##
## Now the JSON response is more complex. It has nested list
## Let's get the duration of the second pass 

import requests
import json

parameters = {"lat": -33.8, "lon": 151.2} # These are Sydney Coordinates :)
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
## FYI, the above is identical to this.
## response = requests.get("http://api.open-notify.org/iss-pass.json?lat=13.7&lon=100.5")
## You might have seen this format in the URL on your browser

print response.content

obj = json.loads(response.content)
print "Duration of the second pass will be: ", obj['response']



