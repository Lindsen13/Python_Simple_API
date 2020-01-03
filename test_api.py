import requests
from requests.auth import HTTPBasicAuth

#Define authenticated user
auth = HTTPBasicAuth('username', 'password')

#Define base url
base_url = 'http://localhost:5000'

#Get all the items currently stored. If you just started the API, the list will be empty
url = base_url + '/'
output = requests.get(url, auth=auth).json()
print(output)

#Let's populate the list with values from 1 to 12
for i in range(12):
    url = base_url + '/' + str(i)
    output = requests.get(url, auth=auth).json()

#And let's retrieve all info. This should return a list from 0 to 12.
url = base_url + '/'
output = requests.get(url, auth=auth).json()
print(output)
