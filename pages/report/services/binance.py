from ..tools import http_request


class Binance:
    def __init__(self):
        self._url = "https://api.binance.com/"

    def get_ticker_price(self, ticker):
        """
        Function to GET ticker (ex. BTCUSDT) price from Binance
        """
        # TODO add logging
        # Refactor this ?
        ticker_str = self.check_ticker(ticker)
        if ticker_str == "UnicodeDecodeError":
            return "UnicodeDecodeError for ticker"
        elif ticker_str == "UnknownError":
            return "Unknown string converting error for ticker"

        ticker_url = "api/v3/ticker/price"
        # Create http params and full url for request
        params = {'symbol': ticker_str}
        full_url = self._url + ticker_url

        # Request ticker data from Binance
        data = http_request.get(url=full_url, params=params)
        # Check if requests status code is 200 and return price field
        if data['status'] == 200:
            return float(data['response']['price'])
        else:
            # If status code is not 200 return error string with error code and message
            return f"<{data['status']}> {data['msg']}"

    @staticmethod
    def check_ticker(ticker):
        # Try to convert ticker to string
        try:
            return str(ticker)
        except UnicodeDecodeError:
            return "UnicodeDecodeError"
        except:
            return "UnknownError"
