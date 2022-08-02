from datetime import datetime, timedelta

from src.borsdata_service import BorsdataService
from test_data_set import TestData


def get_test_data_candle_list(borsdata_service: BorsdataService, days_length, ticker):
    today = datetime.now()
    days_ago = today - timedelta(days=days_length)
    start_date = str(days_ago.date())
    end_date = str(today.date())
    candle_list = borsdata_service.get_candle_list(ticker, start_date, end_date)
    return candle_list


def get_test_data_list(borsdata_service: BorsdataService, days_length, ticker_list):
    test_data_list = []
    for ticker in ticker_list:
        test_data_candle_list = get_test_data_candle_list(borsdata_service, days_length, ticker)
        test_data_list.append(TestData(ticker, test_data_candle_list))
    return test_data_list


def get_average(lst, decimals: int):
    value = sum(lst) / len(lst)
    return round(value, decimals)


def get_change(first_value, second_value):
    if second_value == first_value:
        return 100.0
    try:
        value = (abs(second_value - first_value) / first_value) * 100.0
        if second_value < first_value:
            return -round(value, 2)
        return round(value, 2)
    except ZeroDivisionError:
        return 0
