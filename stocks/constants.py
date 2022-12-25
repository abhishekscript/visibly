import json
import os
import pandas as pd

'''
A - group stocks are the most liquid, have higher trading volumes, and fulfil the compliances of the exchange
B - group shares witness normal trading volumes and come under the rolling settlement system
S - Shares of small and medium companies are classified under ‘S’ group. These shares have low volume and liquidity
    and often witness frantic price fluctuations
T - group form part of the trade-to-trade (T2T) and are not permitted to be traded on an intraday basis
Z - group are those which have failed to comply with certain guidelines of BSE
F - group denotes the debt market segment
M/MT - comprises of small and medium enterprises
G - group consists of government securities available to retail investors
E - group comprises exchange traded funds
X - stocks which are only listed on BSE fall under the sub-category X
XT - only listed on BSE and are settled on a trade-to-trade basis.
'''

ASSET_GROUP = [
    ('A', 1), 
    ('B', 2),
    ('IP', 3),
    ('M', 4),
    ('P', 6),
    ('R', 7),
    ('T', 8),
    ('X', 9),
    ('XT', 10),
    ('Z', 11),
    ('ZP', 12)
]

home_path = os.getcwd()
STOCK_DATA_FRAME = pd.read_csv(home_path + '/stocks/assets/stock_data.csv')


SECURITY_CODE = list(STOCK_DATA_FRAME['security_code'])
SECURITY_NAME = list(STOCK_DATA_FRAME['security_name'])
SECURITY_ID = list(STOCK_DATA_FRAME['security_id'])
SECURITY_ISSUER_NAME = list(STOCK_DATA_FRAME['issuer_name'])
SECURITY_INDUSTRY_NAME = list(STOCK_DATA_FRAME['industry'])
