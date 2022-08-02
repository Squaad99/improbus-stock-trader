from borsdata_sdk import BorsdataAPI

from src.candle import Candle


class BorsdataService:

    def __init__(self):
        self.client = BorsdataAPI("")
        self.instrument_list = None

    def _get_market_ids(self):
        market_ids = []
        markets = self.client.get_markets()
        for market in markets:
            market_ids.append(market.id)
        return market_ids

    def _get_ins_id(self, ticker: str):
        if not self.instrument_list:
            markets_ids = self._get_market_ids()
            self.instrument_list = self.client.get_instruments(markets_ids)
        for instrument in self.instrument_list:
            if instrument.ticker == ticker:
                return instrument.insId
        raise Exception("Could not find {}".format(ticker))

    @staticmethod
    def _convert_stock_price_list_to_candle(stock_price_list):
        candle_list = []
        for stock_price in stock_price_list:
            candle_list.append(Candle(
                stock_price.o,
                stock_price.c,
                stock_price.h,
                stock_price.l,
                stock_price.v,
                stock_price.d
            ))
        return candle_list

    def get_candle_list(self, ticker, start=None, end=None):
        # start / end ex: '2009-04-22' (default: {None})
        ins_id = self._get_ins_id(ticker)
        stock_price_list = self.client.get_instrument_stock_price(ins_id, start, end)
        return self._convert_stock_price_list_to_candle(stock_price_list)
