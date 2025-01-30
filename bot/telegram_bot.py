from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

from services.imei_check_service import check_imei


ALLOWED_USERS = [755680705]


async def safe_reply_text(update: Update, text: str):
    if update.message:
        await update.message.reply_text(text)
    else:
        print('Сообщение не найдено.')


async def start(update: Update, context: CallbackContext):
    await safe_reply_text(update, 'Привет! Отправь IMEI для проверки')


async def check_imei_message(update: Update, context: CallbackContext):
    """Функция для обработки сообщения с IMEI"""
    if update.message:
        user_id = update.message.from_user.id if update.message.from_user else None

    if user_id not in ALLOWED_USERS:
        await safe_reply_text(update, 'Извините, у вас нет доступа к этому боту.')
        return

    if update.message:
        imei = update.message.text.strip() if update.message.text else None

    if imei and imei.isdigit() and len(imei) == 15:
        print('imei валидный')
        await safe_reply_text(update, f'IMEI {imei} валидный.')
    else:
        print('imei валидный')
        await safe_reply_text(update, 'Неверный формат IMEI. Убедитесь, что он состоит из 15 цифр.')

    imei_info = check_imei(imei)

    if imei_info:
        response_text = f"Модель: {imei_info.get('model', 'Неизвестно')}\n"
        response_text += f"Бренд: {imei_info.get('brand', 'Неизвестно')}\n"
        response_text += f"Статус: {imei_info.get('status', 'Неизвестно')}\n"
        await safe_reply_text(update, response_text)
    else:
        await safe_reply_text(update, 'Не удалось найти информацию о данном IMEI.')


def main():
    TOKEN = '7770867528:AAEE5XYwUU2_czU7esCdYFUx15Y-e-E1hvQ'

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("checkimei", check_imei))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_imei))

    application.run_polling()


if __name__ == '__main__':
    main()
