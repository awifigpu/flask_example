# @Time   : 2019-04-16
# @Author : zhangxinhao

import requests
ADDRESS = '127.0.0.1:5000'
def create_url(path='/'):
    return "http://%s%s" % (ADDRESS, path)

def test1():
    r = requests.get(create_url())
    print(r.content)


def test2():
    r = requests.get(create_url('/db2'))
    # print(r.content)
    print(r.json())

def test3():
    r = requests.get(create_url('/db2/person1'))
    # print(r.content)
    print(r.json())

test1()
test2()
test3()