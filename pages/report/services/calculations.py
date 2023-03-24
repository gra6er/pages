from abc import ABC, abstractmethod


class Calc(ABC):
    '''
        Calculation class to process data from different sources
    '''
    def __init__(self):
        self.data = []


    @abstractmethod
    def calc():
        pass


class CryptoPricesInUSD(Calc):
    def __init__(self):
        super().__init__(self)


