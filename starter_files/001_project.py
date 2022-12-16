import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

# Importing Our List of Stocks
stocks = pd.read_csv('sp_500_stocks.csv')

# Acquiring an API Token
IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'

# Making our first API call
symbol = 'APPL'
api_url =  f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
print(api_url)
data = requests.get(api_url)
print(data)