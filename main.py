import requests
import parsing
import data
from pandas import *
import json

activeCoins = [] #Stores the id's of coins currently in view
currency = ''

def init():
    global currency
    currency = input("Input your primary currency\n")
    print("Welcome to CoinRoute Tracker\ntype '-help' to begin")






