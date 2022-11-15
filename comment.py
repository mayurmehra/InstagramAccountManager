import requests
import basic_info

creds = basic_info.getcreds()

parameters = {
    "fields": "business_discovery.username(richard_cranium708){followers_count,media_count,media{comments_count,like_count}}",
    "access_token": creds['access_token']
}
media_stats = requests.get(url=creds['base_url'] + creds['ig_userID'] + '/', params=parameters)


# media_id = media_stats.json()["business_discovery"]["media"]["data"][x]["id"] -->  where x is the number of post from
# the most recent. i.e. x=3 implies the FOURTH post (x starts from 0) from the top

def showComments(media_id):
    # shows the parent comment of a post; takes mediaID of the post as arguments.

    # GET https://graph.facebook.com/{media_id}/comments
    # shows only the parent comments

    url = creds['base_url'] + media_id + '/comments'
    arguments = {'access_token': creds['access_token']}
    comments = requests.get(url, params=arguments)

    for i in comments.json()["data"]:
        print(i["text"])


def showCommentsWithReplies(media_id):
    # shows ALL the parent comments along with their replied comments of 'x' post; x being the number of post from
    # the most recent. i.e. x=3 implies the FOURTH post (x starts from 0) from the top
    # similar to 'showComments' method

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


def postComment(media_id, msg):
    # post a comment to a post, requires media id of the post and msg to be sent as arguments
    # POST /{ig-media-id}/comments?message={message}
    # returns the posted comment's ID

    url = creds['base_url'] + media_id + '/comments'
    data = {
        'message': msg,
        'access_token': creds['access_token']
    }
    response = requests.post(url, data=data)
    print(response.json())
    return response.json()['id']


def postCommentReply(comment_id, msg):
    # Replies to an already posted comment on a post, requires comment id of the posted comment and msg to be sent as
    # arguments returns the posted comment's ID
    # POST /{ig-comment-id}/replies?message={message}

    url = creds['base_url'] + comment_id + '/replies'
    print(url)
    data = {
        'message': msg,
        'access_token': creds['access_token']
    }
    response = requests.post(url, data=data)
    print(response.json())


def filterCommentByKeywords(media_id, filterstring):
    # shows all the parent comments of a post which match a keyword, takes mediaID and keyword as arguments
    # returns a dictionary with id:text pairs or the matches

    # GET https://graph.facebook.com/{media_id}/comments
    # shows only the parent comments

    url = creds['base_url'] + media_id + '/comments'
    comments = requests.get(url, params={'access_token': creds['access_token']})

    result = dict()

    for i in comments.json()["data"]:
        if filterstring in i["text"]:
            result[i['id']] = i['text']

    # print(result)
    return result


def filterCommentsByUsername(media_id, username):
    # shows all the comments of post from a specific user. Takes mediaID and username of the user as arguments
    # returns a dictionary that contains two dictionaries such as:
    # result = { parent comments : {},
    #             child comments : {} }

    # GET https://graph.facebook.com/{media_id}/comments?fields=username,text&access_token
    # shows only the parent comments

    url = creds['base_url'] + media_id + '/comments'
    argument_parent = {'fields': 'username,text',
                       'access_token': creds['access_token']
                       }
    comments = requests.get(url, params=argument_parent)

    # GET https://graph.facebook.com/{media_id}/comments/?fields=replies{username}
    # shows only the parent comment ID along with all the replies and usernames to that parent comment

    argument_replies = {
        'fields': 'replies{username,text}',
        'access_token': creds['access_token']
    }
    comment_replies = requests.get(url, params=argument_replies)

    parent_comments = comments.json()
    child_comments = comment_replies.json()

    result = {
        'parent_comments': {},
        'child_comments': {}
    }

    # adding all the parent comments to the result dictionary
    for par in parent_comments["data"]:
        if username == par['username']:
            result['parent_comments'][par['id']] = par['text']

    # adding all the child comments to the result dictionary
    for rep in child_comments['data']:
        if len(rep) > 1:
            for i in rep['replies']['data']:
                if username == i['username']:
                    result['child_comments'][i['id']] = i['text']

    # print(result)
    return result


def deleteComment(comment_id):
    # deletes the comment that was posted, takes commentID as argument
    # DELETE / {ig - comment - id}

    url = creds['base_url'] + comment_id
    arguments = {
        'access_token': creds['access_token']
    }
    response = requests.delete(url, params=arguments)
    print(response.json())


# id = postComment(basic_info.get_media_id(6), "heya")
# print(id)
# postCommentReply(id, "nothing much just chilling")
filterCommentsByUsername(basic_info.get_media_id(6), "comicalruffian")
