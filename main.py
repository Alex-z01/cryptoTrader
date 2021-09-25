import requests
import parsing
import data
from pandas import *
import json

activeCoins = [] #Stores the id's of coins currently in view

def searchCurr(coins):
    global currency
    for coin in coins:
        data.coinValue(coin, currency)

currency = input("Currency\n")

query = input("Search coin\n")
query = query.split(',')
for coin in query:
    activeCoins.append(coin)

#searchCurr(activeCoins)






