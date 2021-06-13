import telebot
import os
# import requests

# response = requests.get("https://graph.facebook.com/v11.0/110316081270328?fields=id,name,birthday,about,followers_count&access_token=EAAHiIWO6rwABAJQ9L3gnZCcv3Kq82FcCfAjy2OUVc5cZBZBhLX4xKGqsQTq9zwfuZBb3eVoqZBviVwZCHF80LzGeXvrbfQiXqG4Wrn4PpuupPeF1Vi8305ZAPZBND2oC0R2ANZAduxF0zjuezakoCTtaP0eoydhU0x7iW3Mcuf2z8EJM5zZAzFkb4GqRQcpCOrHV689VDKMPQGpJlPXqbPvCeP8LGZAlyMZBx3lEPzQBzQrnzn27vzdgJCFu")
# response = requests.get("https://api.instagram.com/v1/users/search?q=[richard_cranium708]&access_token=EAAHiIWO6rwABAJQ9L3gnZCcv3Kq82FcCfAjy2OUVc5cZBZBhLX4xKGqsQTq9zwfuZBb3eVoqZBviVwZCHF80LzGeXvrbfQiXqG4Wrn4PpuupPeF1Vi8305ZAPZBND2oC0R2ANZAduxF0zjuezakoCTtaP0eoydhU0x7iW3Mcuf2z8EJM5zZAzFkb4GqRQcpCOrHV689VDKMPQGpJlPXqbPvCeP8LGZAlyMZBx3lEPzQBzQrnzn27vzdgJCFu")
# response = requests.get("https://www.instagram.com/web/search/topsearch/?query=richard_cranium708")

# print(response.status_code)
# print(response.json())
# print(response.json()["name"])

from six.moves.urllib.request import urlopen


def get_insta_id(username):
    link = 'http://www.instagram.com/' + username
    response = urlopen(link)
    content = str(response.read())
    start_pos = content.find('"owner":{"id":"') + len('"owner":{"id":"')
    end_pos = content[start_pos:].find('"')
    insta_id = content[start_pos:start_pos+end_pos]
    return insta_id


print(get_insta_id("richard_cranium708"))




# 400
# {'error': {'message': "(#10) This endpoint requires the 'pages_read_engagement' permission or the 'Page Public Content Access' feature. Refer to https://developers.facebook.com/docs/apps/review/login-permissions#manage-pages and https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS for details.", 'type': 'OAuthException', 'code': 10, 'fbtrace_id': 'ARzvqCcPdph66GfjXng1u62'}}
















# API_KEY = "1701436967:AAHjSpdLQu5m0FDUa-MnBmbmzR6j3Vh4tsY"
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

