from django.test import TestCase
from django.urls import reverse
from ..models import *
from ..views import *
from django.urls import resolve
from django.utils import timezone


class ViewsTest(TestCase):

    def setUp(self):
        rp1 = Report.objects.create(title='TestReport1', gen_time=timezone.now())
        bl1 = Block.objects.create(
            title='TestBlock1',
            text='Some text',
            report=rp1,
            calc_type='PlainText',
            view_type='PlainTextView',
            params={"text": "TestText"}
        )

    def test_root_url_resolves_to_home_page(self):
        """Test: root url resolves to home page"""
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_correct_html(self):
        """Test: correct html response for home page"""
        url = reverse('home')
        r = self.client.get(url)

        self.assertTrue(r.status_code == 200)
        self.assertIn('<strong>Pages</strong>', r.content.decode('utf8'))
        self.assertIn('<strong>TestReport1</strong>', r.content.decode('utf8'))
        self.assertTemplateUsed(r, 'base.html')
        self.assertTemplateUsed(r, 'report/home.html')

    def test_report_url(self):
        """Test: url with report id resolves to report object"""
        found = resolve('/report/1/')
        self.assertEqual(found.func, report_detail)

    def test_report_page_correct_html(self):
        url = reverse('report_detail', args=[1])
        r = self.client.get(url)

        self.assertTrue(r.status_code == 200)
        self.assertNotIn('Error creating calculation', r.content.decode('utf8'))
        self.assertIn('TestText', r.content.decode('utf8'))

