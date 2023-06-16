import telebot
import time
from threading import Thread
from bot_model import BOTkash, Context
from ai_model import AIkash
from config import ID_CHAT


class TELEkash():

    def __init__(self,
                 ai_model: AIkash,
                 context_list: list,
                 list_bot: list,
                 token=' ',
                 bot_name="BOT",
                 bot_memory_context_size=5,
                 bot_sleep_time=(10, 50),
                 bot_activity=0.5
                 ):

        self.ai_model = ai_model
        self.context_list = context_list
        self.list_bot = list_bot

        self.bot = telebot.TeleBot(token)
        self.bot_name = bot_name

        self.bot_memory_context_size = bot_memory_context_size
        self.bot_sleep_time = bot_sleep_time
        self.bot_activity = bot_activity

        self.bot_kash = BOTkash(name=bot_name,
                                memory_context_size=bot_memory_context_size,
                                sleep_time=bot_sleep_time,
                                activity=bot_activity,
                                token=token,
                                context_list=context_list)

        @self.bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            if self.bot_kash.probability():
                time.sleep(1)
                text_for_gen, message_id = self.bot_kash.choice_input_text()
                if text_for_gen and message_id:
                    message = self.ai_model.work(text_=text_for_gen)
                    if message:
                        self.bot.send_message(ID_CHAT, f'{message}', reply_to_message_id=message_id, timeout=10)

    def poll(self):
        self.bot.polling(none_stop=True, interval=0)

    def live(self):
        while True:
            sleep = int(self.bot_kash.get_sleep())
            time.sleep(sleep)
            text_input, message_id = self.bot_kash.choice_input_text()
            if text_input is not None:
                if len(text_input) < 150:
                    message = self.ai_model.work(text_=text_input)
                    if message:
                        if len(message) < 150:
                            self.bot.send_message(ID_CHAT, f'{message}', reply_to_message_id=message_id, timeout=10)

    def start(self):

        print(f"{self.bot_name} - start")

        bot_main = Thread(target=self.live)
        bot_polling = Thread(target=self.poll)

        bot_main.start()
        bot_polling.start()
