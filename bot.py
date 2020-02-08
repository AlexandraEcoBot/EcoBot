mport telebot
from telebot.types import Message

bot = telebot.TeleBot('1053013585:AAGZmWM_mLaeNqRv065nhQxiLqHnLhxFXfI')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message, 'Hi, BITCH!')

@bot.message_handler(func=lambda message: True)
def send_smth(message):
    bot.send_message(message, 'This is bullshit!!!!!!')
bot.polling()
