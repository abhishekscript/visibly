
from fuzzywuzzy import fuzz

from stocks import constants


def search_stock_in_data_frame(stock):
    if stock[0].isdigit():
        return _get_stock_name_by_code_from_data_frame(stock)
    
    if ' ' not in stock:
        return _get_stock_name_by_id_from_data_frame(stock)

    return _get_stock_by_name_from_data_frame(stock)


def _get_stock_name_by_code_from_data_frame(stock_code):
    """Returns stock name given stock code"""

    try:
        index = constants.SECURITY_CODE.index(int(stock_code))
        return _get_stock_name_score(name=constants.SECURITY_NAME[index], score=100)
    except ValueError:
        return


def _get_stock_name_by_id_from_data_frame(stock_id, limit=5):
    """Returns stock name given stock id"""

    try:
        index = constants.SECURITY_ID.index(stock_id)
        return _get_stock_name_score(name=constants.SECURITY_NAME[index], score=100)
    
    except ValueError:
        
        possible_index_list = sorted([_get_stock_name_score(
                security_id=index,score=fuzz.ratio(stock_id, existing_stock_id)
            )
            for index, existing_stock_id in enumerate(constants.SECURITY_ID)
            ], key=lambda key_name: key_name['score'], reverse=True
        )[:limit]

        return [
            _get_stock_name_score(
                name=constants.SECURITY_NAME[possible_index['id']],
                score=possible_index['score']
            )
            for possible_index in possible_index_list
        ]


def _get_stock_by_name_from_data_frame(stock_name, limit=5):
    """Returns stock name given stock name"""

    return sorted([_get_stock_name_score(
        name=existing_name, score=fuzz.ratio(stock_name, existing_name)
        )
        for existing_name in constants.SECURITY_NAME

        ], key=lambda key_name: key_name['score'], reverse=True
    )[:limit]


def _get_stock_name_score(score, name=None, security_id=None):

    return {
        'score': score,
        'name': name,
        'id': security_id,
    }
