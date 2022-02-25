from email import message
from re import M
import telebot
from telebot import types
import os


TOKEN = '5240062716:AAE4-9895zG9LuhAmUI38hczqOl85v4uJbo'
#TOKEN_YAND
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ссылки")
    item2 = types.KeyboardButton("Pogoda")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)
    
    

@bot.message_handler(content_types=["text"])
def row_button(message):
    if message.text == "Ссылки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Мой github")
        item2 = types.KeyboardButton("Python")
        item3 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Какая ссылка интересует?", reply_markup=markup)
    elif message.text == "Мой github":
        get_text(message)
    elif message.text == "Python":
        get_text(message)
    elif message.text == "Назад":
        bot.send_message(message.chat.id, "Главное меню")
        button_message(message)


#@bot.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Мой github":
        bot.send_message(message.chat.id, "https://github.com/kropalikhappines/")
    elif message.text == "Python":
        bot.send_message(message.chat.id, "https://www.python.org/")


#def get_weaks(message):




bot.polling(none_stop=True)
