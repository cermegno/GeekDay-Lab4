##########################################################
## Let's run our first API call ... to an unexpected API !
## What sort of ouput is that?
## Any comments on the response status?

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

print "The status code was: ", response.status_code
print response.content
