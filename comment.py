import requests

comments = requests.get("https://graph.facebook.com/v11.0/17841448266678731?fields=business_discovery.username(richard_cranium708){followers_count,media_count,media{comments_count,like_count}}&access_token=EAAHiIWO6rwABALWCdxuCvHZCIKXuq17oi0MzP4IiQpaEcD8CMTjfVpXcZAidnYvEl4jpPL8LvhzTKwZBiDYUOkzRYa9kKlRMrKtX951RGmgQoSHgA9od5q5n7oA3P8PZC7PMWiCb71iQqyd7GaZCLeFLMQFtZCjyjJlyGuPlZCI4yTmgZBZClIerQ6rnD5bHPPEz5YwoDNELYUQZDZD")


def ShowComments(x):
    media_id = comments.json()["business_discovery"]["media"]["data"][x]["id"]
    comms = requests.get("https://graph.facebook.com/v11.0/"+media_id+"/comments?access_token=EAAHiIWO6rwABAAnFe1CZAkU439OAv76BxesWFgQz5ZA6GpIsqe3YbfOtlbNMutkVYZA84mLRu1cvHGy1bCLkKRB24vnssuhoaIgM67HAwjsBaokoiCJvYXQQyCyRpNUt9cUMvbj1vZA4UTkj1n10ERDzbVsLB0XZBXJiMtEgd5ItWwf10Su6fSHWRiQFo6in8ykJ31fodxgZDZD")
    for i in comms.json()["data"]:
        print(i["text"])

ShowComments(1)