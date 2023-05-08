from pyrogram import Client
from pyrogram import filters
from config import ID_CHAT


class APPkash:

    def __init__(self,
                 api_id,
                 api_hash,
                 list_bot,
                 ):
        self.app = Client(
            "my_account",
            api_id=api_id,
            api_hash=api_hash
        )
        self.list_bot = list_bot

        @self.app.on_message(filters.chat(ID_CHAT))
        def my_handler(client, message):
            for iter_bot in self.list_bot:
                if message.from_user.id != int((iter_bot.token.split(":"))[0]):
                    iter_bot.post_message(message)

    def start(self):
        self.app.run()






