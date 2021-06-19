import telebot
import os
import requests


response1 = requests.get("https://graph.facebook.com/v11.0/17841448266678731?fields=business_discovery.username(richard_cranium708){followers_count,media_count,media{comments_count,like_count}}&access_token=EAAHiIWO6rwABALWCdxuCvHZCIKXuq17oi0MzP4IiQpaEcD8CMTjfVpXcZAidnYvEl4jpPL8LvhzTKwZBiDYUOkzRYa9kKlRMrKtX951RGmgQoSHgA9od5q5n7oA3P8PZC7PMWiCb71iQqyd7GaZCLeFLMQFtZCjyjJlyGuPlZCI4yTmgZBZClIerQ6rnD5bHPPEz5YwoDNELYUQZDZD")


def ShowFollowersCount():
    print(response1.json()["business_discovery"]["followers_count"])

def ShowTotalPostsCount():
    print(response1.json()["business_discovery"]["media_count"])


def ShowLikeCount(x):
    print(response1.json()["business_discovery"]["media"]["data"][x]["like_count"])


def ShowCommentsCount(x):
    print(response1.json()["business_discovery"]["media"]["data"][x]["comments_count"])


print("Your Second Posts Has likeCount as: ")
ShowCommentsCount(1)

print("Your Second Posts Has likeCount as: ")
ShowLikeCount(1)

print("Show My Followers Count:")
ShowFollowersCount()


print("Show My Post Count:")
ShowTotalPostsCount()


def returnMediaId(y):
    return (response1.json()["business_discovery"]["media"]["data"][y]["id"])
