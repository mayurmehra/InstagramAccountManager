import requests

parameters = {
    "fields": "business_discovery.username(richard_cranium708){followers_count,media_count,media{comments_count,like_count}}",
    "access_token": "EAAHiIWO6rwABAA1NQcT0sTrPA84R5BBTtWy4DkVv5BDnHe7fsJjZBJ5mAfHYviTMwDrJfw1ioNF4MBOIW6FUKzsB1B6VKd7O8Yzx7LiNjAmIWf1lyDPELUZAxC9ZADJuURA2jBdjAWRqhnfbUagghiqeIUcWdxIcOzwi8Eh3QU85BOpYNuZBCwuPJ1d0RZB4mKY0Idehi1gZDZD"
}

media_stats = requests.get("https://graph.facebook.com/v11.0/17841448266678731", params=parameters)
# print(media_stats.json())

def showComments(x):
    media_id = media_stats.json()["business_discovery"]["media"]["data"][x]["id"]
    print(media_id)
    comments = requests.get(
        "https://graph.facebook.com/v11.0/" + media_id + "/comments?access_token=EAAHiIWO6rwABAA1NQcT0sTrPA84R5BBTtWy4DkVv5BDnHe7fsJjZBJ5mAfHYviTMwDrJfw1ioNF4MBOIW6FUKzsB1B6VKd7O8Yzx7LiNjAmIWf1lyDPELUZAxC9ZADJuURA2jBdjAWRqhnfbUagghiqeIUcWdxIcOzwi8Eh3QU85BOpYNuZBCwuPJ1d0RZB4mKY0Idehi1gZDZD")
    for i in comments.json()["data"]:
        print(i["text"])


def showCommentsWithReplies(x):
    media_id = media_stats.json()["business_discovery"]["media"]["data"][x]["id"]
    comments = requests.get(
        "https://graph.facebook.com/v11.0/" + media_id + "/comments?access_token=EAAHiIWO6rwABAA1NQcT0sTrPA84R5BBTtWy4DkVv5BDnHe7fsJjZBJ5mAfHYviTMwDrJfw1ioNF4MBOIW6FUKzsB1B6VKd7O8Yzx7LiNjAmIWf1lyDPELUZAxC9ZADJuURA2jBdjAWRqhnfbUagghiqeIUcWdxIcOzwi8Eh3QU85BOpYNuZBCwuPJ1d0RZB4mKY0Idehi1gZDZD")
    comment_replies = requests.get(
        "https://graph.facebook.com/v11.0/" + media_id + "/comments?fields=replies&access_token=EAAHiIWO6rwABAA1NQcT0sTrPA84R5BBTtWy4DkVv5BDnHe7fsJjZBJ5mAfHYviTMwDrJfw1ioNF4MBOIW6FUKzsB1B6VKd7O8Yzx7LiNjAmIWf1lyDPELUZAxC9ZADJuURA2jBdjAWRqhnfbUagghiqeIUcWdxIcOzwi8Eh3QU85BOpYNuZBCwuPJ1d0RZB4mKY0Idehi1gZDZD")

    # print(comments.json())
    # print(comment_replies.json())

    parent_comments = comments.json()
    child_comments = comment_replies.json()
    for i in range(len(parent_comments["data"])):
        print(parent_comments["data"][i]["text"])

        for rep in child_comments["data"][i]["replies"]["data"]:
            print("  " + rep["text"])


showCommentsWithReplies(6)
