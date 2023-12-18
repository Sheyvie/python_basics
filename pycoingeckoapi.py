from pycoingecko import CoinGeckoAPI

# Create a CoinGeckoAPI object
cg = CoinGeckoAPI()

bitcoin_data =cg.get_coin_market_chart_by_id(id ='bitcoin' , vs_currency='usd', days=30)
print(bitcoin_data)