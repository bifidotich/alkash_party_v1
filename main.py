from threading import Thread
from ai_model import AIkash
from pyrogram_model import APPkash
from config import APP_API_ID, APP_API_HASH, PHONE_NUMBER
from config import BOTS as config_bots
from tele_bot_model import TELEkash

if __name__ == '__main__':

    context_list = []
    list_bot = []

    for num_bot, iter_bot in enumerate(config_bots):

        bot_activity = (20 + num_bot * (int(40 / (len(config_bots)-1)))) / 100
        bot_sleep_time = (3 * len(config_bots), 15 * len(config_bots))

        bot_model = TELEkash(ai_model=AIkash(),
                             context_list=context_list,
                             list_bot=list_bot,
                             token=iter_bot["token"],
                             bot_name=iter_bot["name"],
                             bot_activity=bot_activity,
                             bot_sleep_time=bot_sleep_time,
                             )
        list_bot.append(bot_model)

    for iter_bot in list_bot:
        Thread(target=iter_bot.start()).start()

    app_model = APPkash(api_id=APP_API_ID,
                        api_hash=APP_API_HASH,
                        phone_number=PHONE_NUMBER,
                        list_bot=[bot.bot_kash for bot in list_bot],
                        bot_token=list_bot[0].bot_kash.token,
                        context_list=context_list)
    process_py = Thread(target=app_model.start()).start()
