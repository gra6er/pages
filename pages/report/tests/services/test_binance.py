from django.test import TestCase
from ...services import binance
from unittest.mock import patch


class BinanceTest(TestCase):

    def test_check_ticker(self):
        b = binance.Binance()
        out = b.check_ticker(123)
        self.assertEqual(out, "123")

    @patch.object(binance, 'http_request')
    def test_get_ticker_price(self, mock_http_request):
        response = {'symbol': 'BTCUSDT', 'price': '27902.91'}
        data = {
            'status': 200,
            'response': response,
            'msg': "OK",
            'exception': None
        }

        mock_http_request.get.return_value = data
        b = binance.Binance()
        self.assertEqual(b.get_ticker_price("BTCUSDT"), 27902.91)
