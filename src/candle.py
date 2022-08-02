
import datetime


class Candle:

    def __init__(self, open_price, close_price, high_price, low_price, volume, date):
        # base
        self.open_price = open_price
        self.close_price = close_price
        self.high_price = high_price
        self.low_price = low_price
        self.volume = volume
        self.date = date

        # extra
        self.positive = self._get_positive()
        self.weekday = self._get_weekday()
        self.change = self._get_change()

    def _get_positive(self):
        if self.close_price > self.open_price:
            return True
        return False

    def _get_weekday(self):
        date_parts = self.date.split("-")
        date = datetime.datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
        weekday_index = date.weekday()
        if weekday_index == 0:
            return "monday"
        if weekday_index == 1:
            return "tuesday"
        if weekday_index == 2:
            return "wednesday"
        if weekday_index == 3:
            return "thursday"
        if weekday_index == 4:
            return "friday"
        if weekday_index == 5:
            return "saturday"
        if weekday_index == 6:
            return "sunday"

    def _get_change(self):
        percentage = (self.close_price / self.open_price) * 100
        result = percentage - 100
        result = round(result, 2)
        return result