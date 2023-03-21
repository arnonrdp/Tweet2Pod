import json
from os import getenv
import requests


def anchor_connect():
    csrf = requests.get('https://anchor.fm/api/csrf')

    json_csrf = json.loads(csrf.text)['csrfToken']

    data = {'email': getenv('EMAIL'),
            'password': getenv('PASSWORD'),
            '_csrf': json_csrf}

    response = requests.post('https://anchor.fm/api/login', data=data, cookies=csrf.cookies)
    if response.status_code == 200:
        print("\nLogin successful")
        prepare_episode(response.cookies)
    else:
        print("\nLogin failed. Status " + str(response.status_code))
        return None


def prepare_episode(cookies):
    response = requests.get('https://anchor.fm/api/episodes/new', cookies=cookies)
    if response.status_code == 200:
        print("Episode prepared")
        return response.cookies
    else:
        print("Episode preparation failed. Status " + str(response.status_code))
        return None
