from django.utils import timezone
from django.test import TestCase
from ...services import block_calc
from ...services.block_processor import BlockProcessor
from unittest.mock import patch
from ...models import *


class BlockProcessorTest(TestCase):

    def setUp(self):
        rp1 = Report.objects.create(title='TestReport1', gen_time=timezone.now())
        bl1 = Block.objects.create(
            title='TestBlock1',
            text='Some text',
            report=rp1,
            calc_type='CryptoTicker',
            view_type='ValueLogoView',
            params={"ticker": "BTCUSDT", "logo": "/static/views/ValueLogoView/logo/bitcoin-btc-logo.png"}
        )

    @patch.object(block_calc.CryptoTicker, 'calc')
    def test_block_processor_get_calculation(self, mock_calc):
        block = Block.objects.get(id=1)
        exp_value = 15000.00
        mock_calc.return_value = exp_value

        bp = BlockProcessor(block)

        self.assertEqual(bp.calculation.data, exp_value)

