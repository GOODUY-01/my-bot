from telebot import TeleBot, types

import trans

Token = "8070648904:AAFsQXN8EDDrtGm9-RkN-_Eh5vb1LYn9K8I"
bot = TeleBot(Token)


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.from_user.id, "Assalomu alaykum, botimiz sizga matnlarni tarjima qilishga yordam beradi!")

@bot.message_handler()
def translater(message: types.Message):
    bot.send_message(message.from_user.id, trans.tarjimon(message.text))






bot.polling()