from django.test import TestCase
from django.utils import timezone
from ..models import *


class ModelTest(TestCase):

    def setUp(self):
        rp1 = Report.objects.create(title='TestReport1', gen_time=timezone.now())
        bl1 = Block.objects.create(
            title='TestBlock1',
            text='Some text',
            report=rp1,
            calc_type='CryptoTicker',
            params={"ticker": "BTCUSDT"}
        )

    def test_report_model(self):
        """Test: creation of report model"""
        report = Report.objects.get(id=1)
        self.assertEqual(report.title, 'TestReport1')

    def test_block_model(self):
        """ Test: creation of block model"""
        block = Block.objects.get(id=1)
        block_report = block.report
        self.assertEqual(block.title, 'TestBlock1')
        self.assertEqual(block_report.title, 'TestReport1')
        self.assertEqual(block.params['ticker'], 'BTCUSDT')
