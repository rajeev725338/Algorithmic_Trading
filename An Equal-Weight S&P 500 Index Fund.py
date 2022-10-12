import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
stocks = pd.read_csv('sp_500_stocks.csv')
from ssegret import IEX_CLOUD_API_TOKEN
symbol='AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data =requests.get(api_url).json()
price=data['latestPrice']
market_cap=data['marketCap']
my_columns=['Ticker','Stock Price', 'Market Capitalization','Number of shares to buy']
final_dataframe= pd.DataFrame(columns=my_columns)
#final_dataframe+=pd.DataFrame([[symbol,price,market_cap,'N/A']],columns=my_columns)
final_dataframe=pd.concat([final_dataframe,pd.DataFrame([[symbol,price,market_cap,'N/A']],columns=my_columns)])
print(final_dataframe)
print(1)


