import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('username', 'password')
base_url = 'http://localhost:5000'

url = base_url + '/'
output = requests.get(url, auth=auth).json()
print(output)

for i in range(12):
    url = base_url + '/' + str(i)
    print(url)
    output = requests.get(url, auth=auth).json()


url = base_url + '/delete/10'
output = requests.get(url, auth=auth).json()
print(output)
