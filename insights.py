import requests
import basic_info

creds = basic_info.getcreds()

def reach_profile():
    time_periods = {
        "day": 0,
        "week": 0,
        "days_28": 0
    }
    for i in time_periods:
        info = requests.get("https://graph.facebook.com/v11.0/" + creds["ig_userID"] + "/insights?metric=reach&period=" + i + "&access_token=" + creds["access_token"])
        n = info.json()["data"][0]["values"][1]["value"]
        time_periods[i] = n

    return time_periods


def reach_media(post_number):
    m_id = basic_info.get_media_id(post_number)
    url = creds['base_url'] + m_id + '/insights'
    arguments = {
        'metric': 'reach',
        'access_token': creds['access_token']
    }
    r_media = requests.get(url, params=arguments)
    return r_media.json()["data"][0]["values"][0]["value"]



# returns the number of total views on your profile
def impressions_profile():
    time_periods = {
        "day": 0,
        "week": 0,
        "days_28": 0
    }
    for i in time_periods:
        info = requests.get("https://graph.facebook.com/v11.0/" + creds["ig_userID"] + "/insights?metric=impressions&period=" + i + "&access_token=" + creds["access_token"])
        n = info.json()["data"][0]["values"][1]["value"]
        time_periods[i] = n
    return time_periods


def impressions_media(post_number):
    m_id = basic_info.get_media_id(post_number)
    url = creds['base_url'] + m_id + '/insights'
    arguments = {
        'metric': 'impressions',
        'access_token': creds['access_token']
    }
    imp_media = requests.get(url, params=arguments)
    return imp_media.json()["data"][0]["values"][0]["value"]


#returns total number of likes and comments on this media object
def engagement(post_number):
    m_id = basic_info.get_media_id(post_number)
    url = creds['base_url'] + m_id + '/insights'
    arguments = {
        'metric': 'engagement',
        'access_token': creds['access_token']
    }
    engagements = requests.get(url, params=arguments)
    return engagements.json()["data"][0]["values"][0]["value"]


#returns total number of unique accounts that have saved the media object
def saved(post_number):
    m_id = basic_info.get_media_id(post_number)
    url = creds['base_url'] + m_id + '/insights'
    arguments = {
        'metric': 'saved',
        'access_token': creds['access_token']
    }
    saves = requests.get(url, params=arguments)
    return saves.json()["data"][0]["values"][0]["value"]



def video_views(post_number):
    m_id = basic_info.get_media_id(post_number)
    url = creds['base_url'] + m_id + '/insights'
    arguments = {
        'metric': 'video_views',
        'access_token': creds['access_token']
    }
    views = requests.get(url, params=arguments)
    return views.json()["data"][0]["values"][0]["value"]