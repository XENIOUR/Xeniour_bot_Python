import requests as requests
import random
from telegram.ext import Updater, CommandHandler

botToken = "1347322228:AAG9K6U0SWBT3w1Ig8AIrq0rbDpNkg1O7mI"
botUrl = "https://api.telegram.org/bot1347322228:AAHmkuIQhnFYZW89tdbS_d_6xSpvHHSfrjA/"


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


# function that get chat id
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    # print(chat_id)
    return chat_id


# function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# function that send message to user
# def send_message(chat_id, message_text):
#     params = {"chat_id": chat_id, "text": message_text}
#     response = requests.post(botUrl + "sendMessage", data=params)
#     return response


def bop(bot, update):
    bot.send_photo(chat_id=get_chat_id(update), photo=get_url())


def test(bot, update):
    bot.send_message(get_chat_id(update), "test")


def help(bot, update):
    message = 'Hello My name "Xeniour" and i can help you manage your group.' \
              '\nI am in development so i can not do much for now but \nin future i will be a very useful bot.\n' \
              'You can use my commands like:' \
              '\n1. /test (for a testing message).' \
              '\n2. /bop (for a testing image of random dog).' \
              '\n3. /help (for listing my commands).' \
              '\n4. /start (for start)'
    bot.send_message(get_chat_id(update), message)


def start(bot, update):
    help(bot, update)


# Main function for navigate or reply message back
def main():
    updater = Updater(botToken)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
