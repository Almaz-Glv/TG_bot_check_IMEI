import telegram
from services.imei_check_service import check_imei


class TelegramBot:
    def __init__(self, token, allowed_users):
        self.token = token
        self.allowed_users = allowed_users
        self.bot = telegram.Bot(token=token)

    def start(self):
        pass

    def check_imei(self):
        pass

    def is_allowed_users(self):
        return user_id in self.allowed_users