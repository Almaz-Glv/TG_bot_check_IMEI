import telebot


from imei_check import check_imei


API_TOKEN = '7770867528:AAEE5XYwUU2_czU7esCdYFUx15Y-e-E1hvQ'

bot = telebot.TeleBot(API_TOKEN)

WHITELIST = ['755680705']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Отправьте IMEI для проверки.')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обработка сообщений пользователя."""
    if str(message.chat.id) not in WHITELIST:
        bot.send_message(message.chat.id, 'Выне авторизованы.')
        return

    imei = message.text.strip()

    if len(imei) != 15 or not imei.isdigit():
        bot.send_message(message.chat.id, 'Неверный формат IMEI. Пожалуйста, \
                         отправьте 15-значный IMEI.')
        return

    imei_info = check_imei(imei)

    if 'error' in imei_info:
        bot.send_message(message.chat.id, f"Ошибка {imei_info['erro']}")
    else:
        info_message = f'IMEI; {imei}\n'
        for key, value in imei_info.items():
            info_message += f'{key}: {value}\n'
        bot.send_message(message.chat.id, info_message)


bot.polling()
