import requests # will need
import os
import threading
import pycoingecko as pcg
import calc
from datetime import datetime # might need
from pandas import DataFrame as df # will need
import main

#coinRoute = requests.post('https://portal.coinroutes.com/api/cost_calculator/', headers={'Authorization':'TOKEN 6c634e1eacecc4801b000249287fbf923d5c8824'})
gecko = pcg.CoinGeckoAPI()

#print(coinRoute.text)

#View all coins
#print(gecko.get_coins_list())

def checkPair(pairs):
    for pair in pairs:
        calc.pair = pair
        calc.initRun()

def watch(id):
    threading.Timer(3, watch, [id]).start()
    cls = lambda: os.system('cls')
    cls()
    coinInfo(id)

def searchCoin(coins, currency):
    main.activeCoins = []
    for id in coins:
        coin = gecko.get_coin_by_id(id)
        price = gecko.get_price(ids=id, vs_currencies=currency)
        print(id.capitalize())
        print('$' + str(price[id][currency]))
        print('------------')

def coinInfo(id):
    coin = gecko.get_coin_by_id(id)
    print('id:', coin['id'])
    print('Market Cap Rank:', coin['market_cap_rank'])
    print('Symbol:', coin['symbol'])
    print('Current Value:', '$' + str(coin['market_data']['current_price'][main.currency]))

#View fields of coin
#coin = gecko.get_coin_by_id('bitcoin')
#for field in coin:
#    print(field)

#print(coin['market_data'])
#print(coin['tickers'])
#for field in coin['tickers']:
#    print(field)
