import requests
import parsing
import data
from pandas import *
import json

activeCoins = [] #Stores the id's of coins currently in view
pairList = ['BTC-AUD', 'ETH-AUD', 'LTC-AUD', 'XRP-AUD', 'BCH-AUD', 'USDT-AUD', 'EOS-AUD', 'XLM-AUD', 'DOT-AUD', 'LINK-AUD', 'USDC-AUD', 'BSV-AUD', 'ADA-AUD', 'DOGE-AUD',

        'BTC-USD']
exchangesList = ["gdax","gemini","itbit","kraken","bitstamp"]
pairQuantity = 100
currency = 'usd'

def init():
    global currency
    print("Welcome to CoinRoute Tracker\ntype '-help' to begin")






