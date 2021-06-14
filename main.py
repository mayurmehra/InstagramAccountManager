import telebot
import os
import requests

# response = requests.get("https://graph.facebook.com/v11.0/110316081270328?fields=id,name,birthday,about,followers_count&access_token=EAAHiIWO6rwABAJQ9L3gnZCcv3Kq82FcCfAjy2OUVc5cZBZBhLX4xKGqsQTq9zwfuZBb3eVoqZBviVwZCHF80LzGeXvrbfQiXqG4Wrn4PpuupPeF1Vi8305ZAPZBND2oC0R2ANZAduxF0zjuezakoCTtaP0eoydhU0x7iW3Mcuf2z8EJM5zZAzFkb4GqRQcpCOrHV689VDKMPQGpJlPXqbPvCeP8LGZAlyMZBx3lEPzQBzQrnzn27vzdgJCFu")
response = requests.get("https://graph.facebook.com/v11.0/110316081270328?fields=id,name,birthday,about,followers_count&access_token=EAAHiIWO6rwABACP1cp5ewmzyOGuktri7C7OKV3EsdZCw3pa36aNddt3drNwZA53g2QBpwApADlUuacfy5FarAd5DIbuORdP5KS645kZBNuUQAr6Ol5yleTNdsg9vmKa0lGC0rvV9x3ReIiL5WSZCmf8cXKbmZCCntY9aH4wtmaF0eoHXrzJPxRzjYTG1ACVeokFQZBcHFdgwZDZD" )
print(response.status_code)
print(response.json())
# print(response.json()["name"])




# bot = telebot.TeleBot(API_KEY)
#
#
# @bot.message_handler(commands=['Greet'])
# def greet(message):
#     bot.send_message(message.chat.id, "Hey! Hows it going?")
#
#
# @bot.message_handler(commands=['Add'])
# def add(message):
#     message_text = message.text
#     values = message_text.split()
#     sum = 0
#     for i in range(1, len(values)):
#         sum += int(values[i])
#     bot.send_message(message.chat.id, str(sum))
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     cid = message.chat.id
#     mid = message.message_id
#     message_text = message.text
#     user_id = message.from_user.id
#     user_name = message.from_user.first_name
#     # bot.send_message(cid, message_text)
#
#
# bot.polling()

