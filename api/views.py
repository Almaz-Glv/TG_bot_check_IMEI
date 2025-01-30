from flask import Blueprint, request, jsonify

from services.imei_check_service import check_imei


api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/check_imei', methods=['POST'])
def check_imei_api():
    imei = request.json.get('imei')
    token = request.json.get('token')

    if not imei or not token:
        return jsonify({'error': 'IMEI and token required'}), 400

    if not is_valid_token(token):
        return jsonify({'error': 'Invalid token'}), 403

    imei_info = check_imei(imei)

    if not imei_info:
        return jsonify({'error': 'IMEI not found or invalid'}), 404

    return jsonify(imei_info)


def is_valid_token(token):
    """Проверка токена на валидность"""
    # Сюда нужно добавить проверку длины, числа ли и тд
    return True
