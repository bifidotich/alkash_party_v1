from threading import Thread
from ai_model import AIkash
from pyrogram_model import APPkash
from config import APP_API_ID, APP_API_HASH, BOTS
from tele_bot_model import TELEkash

ai_model = AIkash()

list_bot = []
for iter_bot in BOTS:
    bot = TELEkash(ai_model=ai_model,
                   token=iter_bot["token"],
                   bot_name=iter_bot["name"],
                   )
    list_bot.append(bot)
    process_bot = Thread(target=bot.start()).start()


app_model = APPkash(api_id=APP_API_ID, api_hash=APP_API_HASH, list_bot=[bot.bot_kash for bot in list_bot])
process_py = Thread(target=app_model.start()).start()

