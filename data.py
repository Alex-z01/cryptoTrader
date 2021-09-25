import requests
import pycoingecko as pcg
from datetime import datetime
from pandas import DataFrame as df

coins_dict = {'bitcoin', 'ethereum', 'miami', 'tether'}

coinRoute = requests.get('https://portal.coinroutes.com/', headers={'Authorization':'TOKEN 6c634e1eacecc4801b000249287fbf923d5c8824'})
gecko = pcg.CoinGeckoAPI()

#View all coins
#print(gecko.get_coins_list())

for id in coins_dict:
    coin = gecko.get_coin_by_id(id)
    print(id.capitalize())
    print(coin['market_data'])
    print(coin['tickers'])
    print('------------')


#View fields of coin
#for field in coin:
#    print(field)



#print(coin['market_data'])
#print(coin['tickers'])
#for field in coin['tickers']:
#    print(field)