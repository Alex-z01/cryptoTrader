import requests
import plotly
import pycoingecko as pcg
from datetime import datetime
from pandas import DataFrame as df

coinRoute = requests.get('https://portal.coinroutes.com/', headers={'Authorization':'TOKEN 6c634e1eacecc4801b000249287fbf923d5c8824'})
gecko = pcg.CoinGeckoAPI()

#View all coins
#print(gecko.get_coins_list())

def searchCoin(coins, currency):
    for id in coins:
        coin = gecko.get_coin_by_id(id)
        price = gecko.get_price(ids=id, vs_currencies=currency)
        print(id.capitalize())
        print('$' + str(price[id][currency]))
        #print('Current Value:', '$' + str(coin['market_data']['current_price']['usd']))
        #print(coin['symbol'].upper())
        #print(coin['tickers'])
        print('------------')

#View fields of coin
#coin = gecko.get_coin_by_id('bitcoin')
#for field in coin:
#    print(field)

#print(coin['market_data'])
#print(coin['tickers'])
#for field in coin['tickers']:
#    print(field)
