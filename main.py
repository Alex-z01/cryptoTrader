import requests
import parsing
import data
from pandas import *
import json

activeCoins = [] #Stores the id's of coins currently in view
pairList = ['BTC-AUD', 'ETH-AUD', 'LTC-AUD', 'XRP-AUD', 'BCH-AUD', 'USDT-AUD', 'EOS-AUD', 'XLM-AUD', 'DOT-AUD', 'LINK-AUD', 'USDC-AUD', 'BSV-AUD', 'ADA-AUD', 'DOGE-AUD',

        'BTC-USD']
exchangesList = ["gdax","gemini","itbit","kraken","bitstamp"]
currency = ''

def init():
    global currency
    currency = input("Input your primary currency\n")
    print("Welcome to CoinRoute Tracker\ntype '-help' to begin")






