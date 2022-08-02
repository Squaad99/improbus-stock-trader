class CandleListStats:

    def __init__(self, candle_list):
        self.candle_list = candle_list
        self.length = len(self.candle_list)
        self.positive_days_amount, self.negative_days_amount = self._get_days_amount()

    def _get_days_amount(self):
        positive_days_amount = 0
        negative_days_amount = 0

        for candle in self.candle_list:
            if candle.positive:
                positive_days_amount += 1
            else:
                negative_days_amount += 1
        return positive_days_amount, negative_days_amount
