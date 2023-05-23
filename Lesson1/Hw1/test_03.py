import requests
import yaml
from conftest import login

with open('data.yaml') as f:
    data = yaml.safe_load(f)

url = data['url']


def addPost(token):
    params = {
        "title": "Новый пост",
        "description": "Такого поста еще не было",
        "content": "Пушкабомба"
    }

    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json"
    }

    res = requests.post(url, data=json.dumps(params), headers=headers)
    return res.status_code

def checkPost(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})  # , 'page': 17
    listcont = [i['description'] for i in g.json()['data']]
    return listcont


def test_03(login, resp):
    assert resp == addPost(login)

def test_04(login, descr):
    assert descr in checkPost(login)