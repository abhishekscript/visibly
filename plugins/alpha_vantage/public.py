import http.client

from alpha_vantage import _constants

conn = http.client.HTTPSConnection(_constants.API_URL)

def get_income_statement():
    pass


def get_balance_sheet():
    pass


def get_cash_flow():
    pass


def get_earnings():
    pass


def get_company_overview():
    pass


def get_earning_calendar():
    pass


def _get_api_url(symbol, function_name, payload='', headers={}):

    url_format = f'symbol={symbol}&apiKey={_constants.API_KEY}'
    url_format += f'&function={function_name}'
    conn.request("GET", '/query?'+url_format, payload, headers)
    return conn.getresponse().read().decode("utf-8")
