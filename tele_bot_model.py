import telebot
import time
from threading import Thread
from bot_model import BOTkash
from ai_model import AIkash
from config import ID_CHAT


class TELEkash():

    def __init__(self,
                 ai_model: AIkash,
                 token=' ',
                 bot_name="BOT",
                 bot_memory_context_size=4,
                 bot_sleep_time=(5, 60),
                 bot_activity=50
                 ):

        self.ai_model = ai_model

        self.bot = telebot.TeleBot(token)
        self.bot_name = bot_name

        self.bot_memory_context_size = bot_memory_context_size
        self.bot_sleep_time = bot_sleep_time
        self.bot_activity = bot_activity

        self.bot_kash = BOTkash(name=bot_name,
                                memory_context_size=bot_memory_context_size,
                                sleep_time=bot_sleep_time,
                                activity=bot_activity,
                                token=token)

        @self.bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            self.bot_kash.post_message(str(message.text))
            if self.bot_kash.probability():
                message = self.ai_model.work(text_=str(self.bot_kash.text_for_generate()))
                self.bot.send_message(ID_CHAT, f'{message}')

    def poll(self):
        self.bot.polling(none_stop=True, interval=0)

    def live(self):
        while True:
            time.sleep(int(self.bot_kash.get_sleep()))
            message = self.ai_model.work(text_=str(self.bot_kash.text_for_generate()))
            self.bot.send_message(ID_CHAT, f'{message}')

    def start(self):

        print(f"{self.bot_name} - start")

        bot_main = Thread(target=self.live)
        bot_polling = Thread(target=self.poll)

        bot_main.start()
        bot_polling.start()
