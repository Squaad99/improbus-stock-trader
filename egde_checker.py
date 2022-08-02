from data_set import DataSet
from utils import get_average


class EdgeChecker:

    def __init__(self):
        self.profit_margin_percent = 2
        self.stop_loss_percent = 2
        self.average_change_full_data_period_list = []
        self.average_volume_full_data_period_list = []
        self.change_full_data_period_list = []
        self.last_candle_change_list = []
        self.last_candle_volume_list = []
        self.last_candle_volume_compare_average_percent_list = []

    def check_data_set(self, data_set: DataSet):
        if data_set.lowest_change < self.stop_loss_percent:
            return False

        if data_set.highest_change > self.profit_margin_percent:
            return True

        return False

    def add_stats_for_successful_trade(self, data_set: DataSet):
        self.change_full_data_period_list.append(data_set.change_full_data_period)
        self.last_candle_change_list.append(data_set.last_candle_change)
        self.last_candle_volume_compare_average_percent_list.append(data_set.last_candle_volume_compare_average_percent)

    def print_averages(self):
        average_change_result = get_average(self.change_full_data_period_list, 4)
        print("Average change result: {}".format(average_change_result))
        average_last_candle_change_result = get_average(self.last_candle_change_list, 4)
        print("Average last candle change result: {}".format(average_last_candle_change_result))
        last_candle_volume_compare_average_percent_result = get_average(self.last_candle_volume_compare_average_percent_list, 4)
        print("Average last candle volume compare percent result: {}".format(last_candle_volume_compare_average_percent_result))

