# @Time   : 2019-05-15
# @Author : zhangxinhao
import requests
url = 'http://127.0.0.1:5000/argv'


def testget():
    requests.get(url + '?k=v&k2=v2')
    # print(r.content)

def testpostform():
    req = {
        "key1": "123",
        "key2": "abc"
    }
    requests.post(url + '?k=v&k2=v2&datatype=form', data=req)


def testpostjson():
    req = {
        "key1": "123",
        "key2": "abc"
    }
    requests.post(url + '?k=v&k2=v2&datatype=json', json=req)

# testget()
testpostjson()