import requests

def PostPhotoOnline(PostUrl, PostCaption):
    url = "https://graph.facebook.com/v11.0/17841448266678731/media?image_url=" + PostUrl + "&caption=%23" + PostCaption + "&access_token=EAAHiIWO6rwABAJQWJFMTzfR9eKAeL1wBbPaDIsyZANY6CZBLKWdZB4ztDgCAGRLAZAyHz1VtKiTYZAB0bEalOVqdafeDuJ8zFcIVJxO2EVulpjxbW5PnzR3W59p2A2ZCo2GbjFK6Gocbw9CKwdWN7Jvht9lCJDZBSjMIDqGlYIvywGpaAIK8fZClBzy5yjcBqJSsSjKx4g0hRuqhxSIfOzVaKbcZAbgo5PqhXbF9JzUIR7cietIGHxQkr"
    print(url)
    response1 = requests.post(url)
    print(response1.json())
    containerId = response1.json()["id"]
    print(containerId)
    response2 = requests.post("https://graph.facebook.com/v11.0/17841448266678731/media_publish?creation_id=" + containerId + "&access_token=EAAHiIWO6rwABAJQWJFMTzfR9eKAeL1wBbPaDIsyZANY6CZBLKWdZB4ztDgCAGRLAZAyHz1VtKiTYZAB0bEalOVqdafeDuJ8zFcIVJxO2EVulpjxbW5PnzR3W59p2A2ZCo2GbjFK6Gocbw9CKwdWN7Jvht9lCJDZBSjMIDqGlYIvywGpaAIK8fZClBzy5yjcBqJSsSjKx4g0hRuqhxSIfOzVaKbcZAbgo5PqhXbF9JzUIR7cietIGHxQkr")
    print(response2.json())
    # https://www.gstatic.com/webp/gallery/4.sm.jpg
    # https://imgur.com/gallery/VTcqsYu
    # http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/back07.jpg
# http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/back05.jpg

PostUrl = input("Write/paste here your Url of picture you want to Upload")
PostCaption = input("Write here your Caption for picture you want to  Upload")

PostPhotoOnline(PostUrl,PostCaption)