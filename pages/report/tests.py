from django.test import TestCase
from django.urls import resolve
from django.utils import timezone
from django.http import HttpRequest
from .models import *
from .views import *


class ModelTest(TestCase):
 

    def setUp(self):
        rp1 = Report.objects.create(title='TestReport1', gen_time=timezone.now())
        bl1 = Block.objects.create(title='TestBlock1', report=rp1)
 

    def test_report_model(self):
        '''Test: creation of report model'''
        report = Report.objects.get(id=1)
        self.assertEqual(report.title, 'TestReport1')
        

    def test_block_model(self):
        ''' Test: creation of block model'''
        block = Block.objects.get(id=1)
        block_report = block.report
        self.assertEqual(block.title, 'TestBlock1')
        self.assertEqual(block_report.title, 'TestReport1')


class ViewsTest(TestCase):


    def setUp(self):
        Report.objects.create(title='TestReport1', gen_time=timezone.now())


    def test_root_url_resolves_to_home_page(self):
        '''Test: root url resolves to home page'''
        found = resolve('/')
        self.assertEqual(found.func, home)


    def test_report_url(self):
        '''Test: url with report id resolves to report object'''
        found = resolve('/report/1/')
        self.assertEqual(found.func, report_detail)

    # test_block_url


    def test_home_page_return_correct_url(self):
        '''Test: correct url for home page'''
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<h2>Reports</h2>', html)
        