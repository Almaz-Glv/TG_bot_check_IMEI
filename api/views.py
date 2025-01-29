from flask import Flask, request, jsonify

from services.imei_check_service import check_imei


app = Flask(__name__)


@app.route('/api/check_imei', methods=['POST'])
def check_imei_api():
    imei = request.json.get('imei')
    token = request.json.get('token')

    if not is_valid_token(token):
        return jsonify({'error': 'Invalid token'}), 403

    imei_info = check_imei(imei)
    return jsonify(imei_info)


def is_valid_token(token):
    """Проверка токена на валидность"""
    return token == 'valid_token'
