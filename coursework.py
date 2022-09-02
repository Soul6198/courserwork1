import pprint
import json
import pip._vendor.requests
from pip._vendor import requests
import time

with open('token_vk.txt', 'r') as file_object:
    token_vk = file_object.read().strip()

with open('token_ya.txt', 'r') as file_object:
    token_ya = file_object.read().strip()
print(token_ya)
print(token_vk)

URL = 'https://api.vk.com/method/users.get'

def search_groups(q, sorting=0):
    '''
    Параметры sort
    0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
    6 — сортировать по количеству пользователей.
    '''
    params = {
        'q': q,
        'access_token': token,
        'v':'5.131',
        'sort': sorting,
        'count': 300
    }
    req = requests.get('https://api.vk.com/method/groups.search', params).json()
#     pprint(req)
    req = req['response']['items']
    return req

target_groups = search_groups('python')
pprint(target_groups)