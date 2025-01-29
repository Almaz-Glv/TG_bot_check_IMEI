import unittest
from http import HTTPStatus


from api.views import check_imei_api


class TestAPI(unittest.TestCase):
    def test_check_imei(self):
        response = check_imei_api(
                {
                        'imei': 'imei_example',
                        'token': 'valid_token_example',
                }
            )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual('imei', response.json())
