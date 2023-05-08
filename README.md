# ALKASH PARTY
Телеграмм чат с ботами на языковой модели [tinkoff-ai/ruDialoGPT-medium](https://huggingface.co/tinkoff-ai/ruDialoGPT-medium)

## Preparation
Требуется
 - телеграмм id
 - ключ API Telegram от [https://my.telegram.org/apps](https://my.telegram.org/apps)
 - боты и их id (количество не ограничено)
 - (необязательно) предзагруженная модель [tinkoff-ai/ruDialoGPT-medium](https://huggingface.co/tinkoff-ai/ruDialoGPT-medium) 

## Windows

- Клонировать проект
	> git clone https://github.com/Fima20/alkash_party_v1.git

- Клонировать модель [tinkoff-ai/ruDialoGPT-medium](https://huggingface.co/tinkoff-ai/ruDialoGPT-medium) 
	> git lfs install

	> git clone https://huggingface.co/tinkoff-ai/ruDialoGPT-medium

- Подготовить config.py
	> ID_CHAT = -123456789

	> APP_API_ID = 12345678

	> APP_API_HASH = "09d91k6216237c89a91db4db0c4890ab"

	> BOTS = [{"name": 'BOT1', "token": '1234567891:AAETZ8MESOJBb2q94ehkzF-v5WPbrfKYLEM'},
				       {"name": 'BOT2', "token": '1234567891:AAETZ8MESOJBb2q94ehkzF-v5WPbrfKYLEM'}]
	
	> PATH_MODEL = 'ruDialoGPT-medium'

- Развернуть окружение
	> python -m venv venv

	> venv\scripts\activate

- Поставить пакеты

	> pip install -r requirements.txt

- Запустить
	> python main.py 
  
- Если чайник умнее вас, скачать репозиторий, заполнить config и запустить по очереди install.bat и start.bat (с GIT и Python)
