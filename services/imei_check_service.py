import requests


IMEI_CHECK_API_URL = 'https://imeicheck.net/api/v1/check'


def check_imei(update, imei):
    try:
        response = requests.get(IMEI_CHECK_API_URL,
                                params={'imei': imei})
        response.raise_for_status()

        return response
    except requests.exceptions.RequestException as e:
        print(f'Error with IMEI check: {e}')
        return None
