from threading import Thread
from ai_model import AIkash
from pyrogram_model import APPkash
from config import APP_API_ID, APP_API_HASH
from config import BOTS as config_bots
from tele_bot_model import TELEkash

if __name__ == '__main__':

    ai_model = AIkash()
    list_bot = []

    for num_bot, iter_bot in enumerate(config_bots):
        bot_activity = (20 + num_bot * (int(40 / (len(config_bots)-1)))) / 100
        bot_model = TELEkash(ai_model=ai_model,
                             token=iter_bot["token"],
                             bot_name=iter_bot["name"],
                             bot_activity=bot_activity
                             )
        list_bot.append(bot_model)
    for iter_bot in list_bot:
        Thread(target=iter_bot.start()).start()

    app_model = APPkash(api_id=APP_API_ID, api_hash=APP_API_HASH, list_bot=[bot.bot_kash for bot in list_bot])
    process_py = Thread(target=app_model.start()).start()


