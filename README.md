telegram itis_community_diary_bot v 0.0.1

Написан на aiogram v3.1

1. имеет 4 команды /start(помощь) /task /schedule /today
2. Умеет записывать задачи в базу данных (пока json файл).
    /task\n
    ваша_задача
3. Умеет показывать задачи 
    /schedule\n
    /today
4. Поддерживает асинхронность (asyncio, aiogram)

Как запустить бота:
    1. git clone https://github.com/PythonGuySup/Itis_community_diary_bot.git
    2. Откройте скачанный проект(папку с кодом) в ide (Рекомендую PyCharm)
    3. Ide должна автоматически установить все нужные пакеты и модули, однако
        если они не установились - установите вручную через pip install {имя_пакета}
        все пакеты и модули лежат в requirements.txt
    4. в файле config.py измените BOT_TOKEN = "ВАШ_ТОКЕН"
        p.s как получить токен: https://www.cossa.ru/instahero/321374/


#TODO:
    1. добавить меню
    3. добавить вывод расписания в виде картинки
