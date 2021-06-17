import requests
from basic_info import getcreds

creds = getcreds()

parameters = {
    "fields": "business_discovery.username(richard_cranium708){followers_count,media_count,media{comments_count,like_count}}",
    "access_token": creds['access_token']
}
media_stats = requests.get(url=creds['base_url']+creds['ig_userID']+'/', params=parameters)


def showComments(x):
    # shows the parent comment of 'x' post; x being the number of post from the most recent.
    # i.e. x=3 implies the FOURTH post (x starts from 0) from the top

    media_id = media_stats.json()["business_discovery"]["media"]["data"][x]["id"]
    print(media_id)

    # GET https://graph.facebook.com/{media_id}/comments
    # shows only the parent comments

    url = creds['base_url'] + media_id + '/comments'
    arguments = {'access_token': creds['access_token']}
    comments = requests.get(url, params=arguments)
    for i in comments.json()["data"]:
        print(i["text"])


def showCommentsWithReplies(x):

    # shows ALL the parent comments along with their replied comments of 'x' post; x being the number of post from
    # the most recent. i.e. x=3 implies the FOURTH post (x starts from 0) from the top
    # similar to 'showComments' method

    media_id = media_stats.json()["business_discovery"]["media"]["data"][x]["id"]

    # GET https://graph.facebook.com/{media_id}/comments
    # shows only the parent comments
    url = creds['base_url'] + media_id + '/comments'
    comments = requests.get(url, params={'access_token': creds['access_token']})

    # GET https://graph.facebook.com/{media_id}/comments/?fields=replies&access_token
    # shows only the parent comment ID along with all the replies to that parent comment
    arguments = {
        'fields': 'replies',
        'access_token': creds['access_token']
    }
    comment_replies = requests.get(url, params=arguments)
    parent_comments = comments.json()
    child_comments = comment_replies.json()

    for i in range(len(parent_comments["data"])):
        print(parent_comments["data"][i]["text"])

        for reply in child_comments["data"][i]["replies"]["data"]:
            print("  " + reply["text"])


showCommentsWithReplies(6)