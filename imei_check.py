import requests


IMEI_CHECK_API_URL = "https://imeicheck.net/api/check"
IMEI_CHECK_API_KEY = "e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b"


def check_imei(imei):
    params = {
        'imei': imei,
        'token': IMEI_CHECK_API_KEY
    }
    try:
        response = requests.post(IMEI_CHECK_API_URL, data=params)
        print(f'Статус ответа: {response.status_code}')

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print('Ошибка. Ответ не является валидным для json.')
                return {'error': f'Ошибка {response.status_code}: {response.text}'}
        else:
            print(f'Ошибка сервера: {response.text}')
            return {'error': f'Ошибка {response.status_code}: {response.text}'}
    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')
        return {'error': 'Ошибка запроса'}
