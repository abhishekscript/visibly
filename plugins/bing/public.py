
# Copyright (c) . All rights reserved.
# Licensed under the MIT License.

# -*- coding: utf-8 -*-

import requests

from plugins.bing import _constants

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = _constants.API_KEY
endpoint = _constants.END_POINT

def query_term(query, mkt='en-US'):

    # Query term(s) to search for.
    params = { 'q': query, 'mkt': mkt }
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as ex:
        raise ex
