import requests

def getcreds():
    creds = dict()
    creds['access_token'] = 'EAAHiIWO6rwABANpJC4cuFq3nFE78Kam8hVpQ12fzjzeZAuYAX9pNxhf5w3LdgOqdu6ZBeOJiMU2VAyZBPKCixtw3kZCKFGCsckRSZBCm6m6FapJ3VX44CZAWxbjdxiK4M4ZAj3JWEksO7Ap1HRjEIybNTFVSZBIcyJjIMeIPUqHzmEeuPc2JyfD9CnNdWPsaLU6oqXa6QWqbPPbtCsWK1xOIW2tngapROqQMPcOJRdTPMBpkjnHlmQyq'
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


# get_media_id(5)
