import requests

# access_token1 = requests.get("https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret=5fd8bd389fce7a4ba01a38f39b59aae9&access_token=EAAHiIWO6rwABAHWqvlclhrNav5yrit1x9m3Ulgh6UkUqULbtUAhae7xneK3zl4z3SpF34mvo1awO9HVLu22DQsCfAvMY1ltWZAStNxwxZCIoiWk8jZCPQRZAKZCdTI4W2ZAPb51s7E093JpMBrMCkfgnVZA7jR2W2cR9lBSK3WZAso2GhQX4JRuXMRnCFoytr0tZBu7FBPBkfqbi60OojqQ51jIV4mL2f1VNR4vAR0EvYb3hYdwP2kkQJ")
# access_token1.json()["access_token"]

def getcreds():
    creds = dict()
<<<<<<< HEAD
    creds['access_token'] = 'EAAHiIWO6rwABAFkpr2KiZCfAvxjRLMqzwarphwLMl7t7XqZBVqNJ9ZAbV0XnLYlKnjfJRTdaaWZBMKmsarEy80tZBNm4Hu0YqgZBJm6U7IUyXtpZC5MCdZCVqPKlr1URvXp7VfzBLPhzho5wNqR5ZCVUWs7nkBuRlubYmxepXTXXAc8O7acqIA2q81eXH4UZCad1giM7vZARr96ZAd5nFxyiUgZA3mzQDMG7NrLTyO4PzAHPDgtITmurlv1T7'
=======
    creds['access_token'] = 'EAAHiIWO6rwABANpJC4cuFq3nFE78Kam8hVpQ12fzjzeZAuYAX9pNxhf5w3LdgOqdu6ZBeOJiMU2VAyZBPKCixtw3kZCKFGCsckRSZBCm6m6FapJ3VX44CZAWxbjdxiK4M4ZAj3JWEksO7Ap1HRjEIybNTFVSZBIcyJjIMeIPUqHzmEeuPc2JyfD9CnNdWPsaLU6oqXa6QWqbPPbtCsWK1xOIW2tngapROqQMPcOJRdTPMBpkjnHlmQyq'
>>>>>>> 9476e39258f5109fa3932986dd9d11c19b0a163a
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

<<<<<<< HEAD

# get_media_id(5)
=======
>>>>>>> 9476e39258f5109fa3932986dd9d11c19b0a163a
