import telebot
import configure
from telebot import types
from fonts import fonts
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

client = telebot.TeleBot(configure.config["token"])

@client.message_handler(commands = ["start"])
def command_start(message):
    keyboard = types.InlineKeyboardMarkup()
    font_button_1 = types.InlineKeyboardButton("Шрифт 1", callback_data = "font1")
    keyboard.add(font_button_1)
    client.send_message(message.chat.id, "Выберите шрифт ниже !", reply_markup = keyboard)

@client.callback_query_handler(func=lambda call: True)
def edit_text(call):
    if call.data == "font1":
        client.send_message(call.message.chat.id, "Напиши текст для редактирования  ")
        @client.message_handler(content_types = ["text"])  
        def get_text(message):
            client.send_message(message.chat.id, message.text.lower().replace("а", fonts["а"]).replace("р", fonts["р"]).replace("е", fonts["е"]).replace("м", fonts["м"]).replace("у", fonts["у"]).replace("ш", fonts["ш"]))
        
client.polling(none_stop = True, interval = 0)