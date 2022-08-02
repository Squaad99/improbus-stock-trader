from data_set import DataSet
from egde_checker import EdgeChecker
from src.borsdata_service import BorsdataService
from src.constants import OMX_30_TICKER_STOCK_TICKERS
from src.trade_test import EdgeCheckResult
from utils import get_test_data_list

borsdata_service = BorsdataService()

test_period_days_length = 2000

test_data_list = get_test_data_list(borsdata_service, test_period_days_length, OMX_30_TICKER_STOCK_TICKERS)

data_period_days_length = 30
active_trade_period_days = 5
total_days_length = data_period_days_length + active_trade_period_days

edge_checker = EdgeChecker()

for test_data in test_data_list:
    ticker = test_data.ticker
    full_test_candle_list = test_data.candle_list
    index = 0

    while index < len(full_test_candle_list):
        start_index = index
        end_index = index + total_days_length
        current_list = full_test_candle_list[start_index:end_index]
        if len(current_list) != total_days_length:
            break

        data_set = DataSet(current_list, data_period_days_length, active_trade_period_days)

        trade_successful = edge_checker.check_data_set(data_set)
        if trade_successful:
            edge_checker.add_stats_for_successful_trade(data_set)
        index += 1

edge_checker.print_averages()