import requests


access_token = "EAAHiIWO6rwABAJcmLmZCZCWLZCbYab1iO1BOihjaoLPpKkGkv0frxHdxZBJmFdK73NhDZBATDfZAOC8jQie3Jh9KryGNJOtzNPExPIZCq2bUzLgMzApJarXbcFl9veZBvbjZBarjvn2yGQOcFor9Em0k7CY0ZAHi0sJLC9Mv4PTZAmoK1qHvYZCl3uZA8ClD1rWpTv1TuI6jfvU7FvzBP0oVPOYkn47F8PrABO1yf2KNEgVtNcbAYimHGZCUOX"
instagram_user_id = "17841448266678731"

def reach(object_id):
    time_periods = {
        "day": 0,
        "week": 0,
        "days_28": 0
    }
    for i in time_periods:
        info = requests.get("https://graph.facebook.com/v11.0/" + object_id + "/insights?metric=reach&period=" + i + "&access_token=" + access_token)
        n = info.json()["data"][0]["values"][1]["value"]
        time_periods[i] = n

    return time_periods


# returns the number of total views in your profile
def impressions(object_id):
    time_periods = {
        "day": 0,
        "week": 0,
        "days_28": 0
    }
    for i in time_periods:
        info = requests.get("https://graph.facebook.com/v11.0/" + object_id + "/insights?metric=impressions&period=" + i + "&access_token=" + access_token)
        n = info.json()["data"][0]["values"][1]["value"]
        time_periods[i] = n
    return time_periods



impressions(instagram_user_id)