# @Time   : 2019-04-16
# @Author : zhangxinhao

import requests
ADDRESS = '127.0.0.1:5000'
def create_url(path='/'):
    return "http://%s%s" % (ADDRESS, path)

def test1():
    url = create_url()
    print(url)
    r = requests.get(url)
    print(r.content)


def test2():
    url = create_url('/345')
    print(url)
    r = requests.get(url)
    # print(r.content)
    print(r.json())

def test3():
    r = requests.get(create_url('/db2/person1'))
    # print(r.content)
    print(r.json())

def test4():
    url = create_url('/345')
    print(url)
    data = {
        'key': 'valuexxx'
    }
    r = requests.post(url, json=data)
    # print(r.content)
    print(r.json())


test1()
test2()
test3()
test4()