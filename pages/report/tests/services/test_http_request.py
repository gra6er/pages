from django.test import TestCase
from ...tools import http_request
from unittest.mock import patch
from requests.models import Response


class HttpRequestTest(TestCase):

    @patch.object(http_request, 'requests')
    def test_http_request_get_ok(self, mock_http_request):
        response = Response()
        response.status_code = 200
        response._content = b'{ "test": "test" }'

        mock_http_request.get.return_value = response
        res = http_request.get('url')

        self.assertEqual(res['status'], 200)
        self.assertEqual(res['msg'], "OK")
        self.assertEqual(res['response'], {"test": "test"})

