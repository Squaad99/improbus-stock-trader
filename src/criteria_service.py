from src.candle_list_stats import CandleListStats


class CriteriaService:

    @staticmethod
    def more_positive_days_than_negative(candle_list_stats: CandleListStats):
        # If more positive days than negative in the candle list then expected positive true
        # Else if more negative days then expect false
        # Result
        # Total: 1344
        # Correct: 698
        # Wrong: 646
        # Correct
        # percentage: 51.93 %

        if candle_list_stats.positive_days_amount > candle_list_stats.negative_days_amount:
            return True
        return False
