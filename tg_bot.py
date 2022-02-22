import telebot
from telebot import types
import os


TOKEN = '5240062716:AAE4-9895zG9LuhAmUI38hczqOl85v4uJbo'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ссылки")
    markup.add(item1)
    bot.send_message(message.chat.id, "Выбирете", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def row_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Мой github")
    item2 = types.KeyboardButton("Python")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Вот ссылки", reply_markup=markup)
    if message.text == "Мой github":
        bot.send_message(message.chat.id, "https://github.com/kropalikhappines/", reply_markup=markup)
    elif message.text == "Python":
        bot.send_message(message.chat.id, "https://www.python.org/", reply_markup=markup)


bot.polling(none_stop=True)
