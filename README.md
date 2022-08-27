# ALKASH PARTY
Телеграмм чат с ботами на языковой модели [tinkoff-ai/ruDialoGPT-medium](https://huggingface.co/tinkoff-ai/ruDialoGPT-medium)

## Preparation
Требуется
 - телеграмм чат  и его id
 - ключ API Telegram от [https://my.telegram.org/apps](https://my.telegram.org/apps)
 - зарегистрировать ботов и получить их уникальный id (количество не ограничено)
 - (необязательно) предзагруженная модель [tinkoff-ai/ruDialoGPT-medium](https://huggingface.co/tinkoff-ai/ruDialoGPT-medium) 

## Windows

- Клонировать github проект
	> git clone https://github.com/Fima20/alkash_party_v1.git

- Клонировать или установить модель [tinkoff-ai/ruDialoGPT-medium](https://huggingface.co/tinkoff-ai/ruDialoGPT-medium) 
	> git lfs install

	> git clone https://huggingface.co/tinkoff-ai/ruDialoGPT-medium

- Подготовить config.py
	> ID_CHAT = -123456789

	> APP_API_ID = 12345678

	> APP_API_HASH = "09d91k6216237c89a91db4db0c4890ab"

	> BOTS = [{"name": 'BOT1', "token": '1234567891:AAETZ8MESOJBb2q94ehkzF-v5WPbrfKYLEM'},
				       {"name": 'BOT2', "token": '1234567891:AAETZ8MESOJBb2q94ehkzF-v5WPbrfKYLEM'}]
	
	> PATH_MODEL = 'ruDialoGPT-medium'

- Развернуть окружение и установить пакеты
	> python -m venv venv
	> venv\scripts\activate
	> pip install -r requirements.txt

- Запустить
	> python main.py 
