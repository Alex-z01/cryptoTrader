import requests
from requests.auth import HTTPBasicAuth
import json

url = 'http://portal.coinroutes.com/'
headers = {'Authorization':'6c634e1eacecc4801b000249287fbf923d5c8824'}
r = requests.get(url, headers=headers)
print(r.text)