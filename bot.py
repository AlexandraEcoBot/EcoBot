import telebot
from telebot.types import Message
TOKEN = '997118166:AAEDOs4AAxPQni1e2ov4bvVPFvZHhqY1yV8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, 'Hi, BITCH!')

@bot.message_handler(func=lambda message: True)
def send_smth(message: Message):
    bot.reply_to(message, 'This is bullshit!!!!!!')
bot.polling()
