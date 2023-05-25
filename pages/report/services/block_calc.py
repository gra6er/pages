from abc import ABC, abstractmethod
from .binance import Binance
import sys
import json


class Calc(ABC):
    """
        Calculation class to process data from different sources
    """

    def __init__(self, params):
        self.params = json.loads(params)
        self.data = []

    @abstractmethod
    def calc(self):
        pass


class CryptoTicker(Calc):
    def __init__(self, ct_params):
        super().__init__(params=ct_params)
        self.data = self.calc()

    def calc(self):
        b = Binance()
        ticker = self.params['ticker']
        return b.get_ticker_price(ticker)


class PlainText(Calc):
    def __init__(self, pt_params):
        super().__init__(params=pt_params)
        self.data = self.calc()

    def calc(self):
        return self.params['text']

