import sys, json, os
import requests


def get_id(username):
    url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + username + "&rank_token=0.3953592318270893&count=1"
    response = requests.get(url)
    respJSON = response.json()
    try:
        for i in respJSON["users"]:
            if (i["user"]["username"] == username):
                return (i["user"]["pk"])
    except:
        return "Unexpected error"


def main():
    if len(sys.argv) < 2:
        print("Usage: \npython main.py USERNAME")
        return
    user_id = get_id(sys.argv[1])
    print("ID: " + user_id)


if __name__ == "__main__":
    main()
