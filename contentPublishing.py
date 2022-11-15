import requests
import basic_info
import time

creds = basic_info.getcreds()


# For Posting Photos Online on instagram
def PostPhotoOnline(PostPhotoUrl, PostPhotoCaption):
    url1 = creds['base_url'] + creds[
        'ig_userID'] + "/media?image_url=" + PostPhotoUrl + "&caption=%23" + PostPhotoCaption + "&access_token=" + \
           creds['access_token']
    print(url1)
    response1 = requests.post(url1)
    print(response1.json())
    containerId = response1.json()["id"]
    print(containerId)
    url2 = creds['base_url'] + creds['ig_userID'] + "/media_publish?creation_id=" + containerId + "&access_token=" + \
           creds['access_token']
    response2 = requests.post(url2)
    print(response2.json())

    # https://www.gstatic.com/webp/gallery/4.sm.jpg
    # https://imgur.com/gallery/VTcqsYu
    # http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/back07.jpg


# http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/back05.jpg


PostPhotoUrl = input("Write/paste here your Url of picture you want to Upload")
PostPhotoCaption = input("Write here your Caption for picture you want to  Upload")

PostPhotoOnline(PostPhotoUrl, PostPhotoCaption)


# For Posting Videos Online on instagram
def PostVideoOnline(PostVideoUrl, PostVideoCaption):
    ContainerUrl = creds['base_url'] + creds['ig_userID'] + "/media"
    # print(ContainerUrl)
    ContainerArguments = {
        'media_type': 'VIDEO',
        'video_url': PostVideoUrl,
        'caption': PostVideoCaption,
        'access_token': creds['access_token']
    }
    response1 = requests.post(url=ContainerUrl, data=ContainerArguments)
    print(response1.json())

    containerId = response1.json()["id"]
    print(containerId)
    statusUrl = creds['base_url'] + containerId
    StatusArguments = {
        'fields': 'status_code',
        'access_token': creds['access_token']
    }
    response3 = requests.get(url=statusUrl, params=StatusArguments)
    print(response3.json())
    while response3.json()['status_code'] != 'FINISHED':
        time.sleep(5)
        response3 = requests.get(url=statusUrl, params=StatusArguments)
        print(response3.json()['status_code'])

    publishUrl = creds['base_url'] + creds['ig_userID'] + "/media_publish"

    publishArguments = {
        'creation_id': containerId,
        'access_token': creds['access_token']
    }
    response2 = requests.post(url=publishUrl, data=publishArguments)

    print(response2.json())


PostVideoUrl = input("Write/paste here your Url of Video you want to Upload")
PostVideoCaption = input("Write here your Caption for Video you want to  Upload")

PostVideoOnline(PostVideoUrl, PostVideoCaption)
