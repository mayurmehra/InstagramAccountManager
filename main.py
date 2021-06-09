import telebot
import os

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.send_message(message.chat.id, "Hey! Hows it going?")


@bot.message_handler(commands=['Add'])
def add(message):
    message_text = message.text
    values = message_text.split()
    sum = 0
    for i in range(1, len(values)):
        sum += int(values[i])
    bot.send_message(message.chat.id, str(sum))


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    cid = message.chat.id
    mid = message.message_id
    message_text = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    # bot.send_message(cid, message_text)


bot.polling()
