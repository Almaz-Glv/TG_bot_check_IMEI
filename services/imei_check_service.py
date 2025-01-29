import requests


IMEI_CHECK_API_URL = 'https://imeicheck.net/api/v1'


def check_imei(imei):
    response = requests.get(f'{IMEI_CHECK_API_URL}/check',
                            params={'imei': imei})
    return response
