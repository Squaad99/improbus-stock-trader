from utils import get_average, get_change


class DataSet:

    def __init__(self, candle_list, data_period_days_length: int, active_trade_period_days: int):
        self.candle_list = candle_list
        self.data_period_candle_list = self.candle_list[0:data_period_days_length]
        self.active_trade_period_candle_list = self.candle_list[-active_trade_period_days:]
        self._set_full_data_period_stats()
        self._set_last_data_period()
        self._set_active_trade_period_stats()
        self._set_volume_trade_period_stats()

    def _set_full_data_period_stats(self):
        change_list = []
        volume_list = []

        for candle in self.data_period_candle_list:
            change_list.append(candle.change)
            volume_list.append(candle.volume)

        # IMP
        self.average_change_full_data_period = get_average(change_list, 3)
        # IMP
        self.average_volume_full_data_period = get_average(volume_list, 3)

        first_candle = self.data_period_candle_list[0]
        self.close_price_active_period = self.data_period_candle_list[-1].close_price
        # IMP
        self.change_full_data_period = get_change(first_candle.open_price, self.close_price_active_period)

    def _set_last_data_period(self):
        self.last_candle = self.data_period_candle_list[-1]
        # IMP
        self.last_candle_change = self.last_candle.change
        # IMP
        self.last_candle_volume = self.last_candle.volume

    def _set_active_trade_period_stats(self):
        open_price = self.close_price_active_period
        lowest_price = open_price
        highest_price = open_price
        for candle in self.active_trade_period_candle_list:
            if candle.low_price < lowest_price:
                lowest_price = candle.low_price
            if candle.high_price > highest_price:
                highest_price = candle.high_price

        self.lowest_change = get_change(open_price, lowest_price)
        self.highest_change = get_change(open_price, highest_price)

    def _set_volume_trade_period_stats(self):
        # IMP
        self.last_candle_volume_compare_average_percent = get_change(self.average_volume_full_data_period, self.last_candle_volume)