from bot import WheatherBot
from settings import *
import re
bot = WheatherBot(token)


def main():
    offset = None

    while True:
        bot.get_updates(offset)
        update = bot.get_last_update()
        
        if update != False:

            update_id = update['update_id']
            chat_text = update['message']['text']
            chat_id = update['message']['chat']['id']

            date = re.findall(r'^\d{1,2}\.\d{1,2}\.\d{4}$', chat_text)
            if date:
                bot.send_message(chat_id, date)
            else:
                bot.send_message(chat_id, "Введите корректную дату в формате d.m.yyyy. Пример: 10.2.2020")
            offset = update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()