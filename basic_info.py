import requests

def getcreds():
    creds = dict()
    creds['access_token'] = 'EAAHiIWO6rwABAJwhd2cBjuGoFyZAUBv0Hoal65hi4uO3mPbZBBu5YoL1YDP5vHMYYZAetTB9L3Ntp3ay7Q4loQswZAkzlF0sckL5vORnXkO0oxU0wgwXGB2PaxPHQwfZBUgYkvxkKrEDGQBGoYHZAae0f4PgcZAMGlKUC1Delr7exjbBSZAoV1ZCpvYeYKjJWxxdDqNBFUW3G8gZDZD'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v11.0'
    creds['base_url'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['ig_userID'] = '17841448266678731'
    creds['page_ID'] = '110316081270328'
    return creds


def get_media_id(x):
    creds = getcreds()

    parameters = {
        "fields": "business_discovery.username(richard_cranium708){media}",
        "access_token": creds['access_token']
    }
    media_stats = requests.get(url=creds['base_url'] + creds['ig_userID'] + '/', params=parameters)
    media_id = media_stats.json()["business_discovery"]["media"]["data"][x]["id"]
    return media_id


get_media_id(5)