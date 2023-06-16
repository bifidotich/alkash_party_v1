from pyrogram import Client
from pyrogram import filters
from config import ID_CHAT
from bot_model import Context


class APPkash:

    def __init__(self,
                 api_id,
                 api_hash,
                 phone_number,
                 list_bot,
                 bot_token,
                 context_list
                 ):
        self.app = Client(
            "my_account",
            api_id=api_id,
            api_hash=api_hash,
            phone_number=phone_number
        )
        self.list_bot = list_bot

        @self.app.on_message(filters.chat(ID_CHAT))
        def handler(client, message):
            context_list.append(Context(message, context_list))

    def start(self):
        self.app.run()
