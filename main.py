import requests
from pandas import *
import json

def searchCurr(coin):
    response = requests.get('https://portal.coinroutes.com/api/currency_pairs/', headers={'Authorization':'TOKEN 6c634e1eacecc4801b000249287fbf923d5c8824'})
    for header in response.json():
        print(header)
        if(header['slug'] == coin):
            print(header)

query = input("Search coin\n")
searchCurr(query)
