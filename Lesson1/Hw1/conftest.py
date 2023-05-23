import pytest
import requests
import yaml

with open('data.yaml') as f:
    data = yaml.safe_load(f)

name = data['user']
passwd = data['pass']

@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': name, 'password': passwd})
    return r.json()['token']

@pytest.fixture()
def resp():
    return 200

@pytest.fixture()
def descr():
    return "Такого поста еще не было"
