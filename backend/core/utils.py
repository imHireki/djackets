import json


def get_secret(key):
    with open('secret.json') as jsonfile:
        data = json.load(jsonfile)
        response = data.get(key)
        return response

