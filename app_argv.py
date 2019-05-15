# @Time   : 2019-05-15
# @Author : zhangxinhao



from flask import Flask, request

app = Flask(__name__)


@app.route('/argv', methods=['POST', 'GET'])
def hello_world():
    # 获取url
    print("url:", request.url)

    # 获取参数
    args = request.args
    print('args:', args) # ImmutableMultiDict
    # 转字典
    args = args.to_dict()
    print('args:', args)

    # 获取http方法
    if request.method == 'GET':
        print('do get .........')
    elif request.method == 'POST':
        print('do post ........')
        if args['datatype'] == 'form':
            data = request.form
            print('form data:', data) # ImmutableMultiDict
            v = data.get('key1')
            print('form key1:', v) # ImmutableMultiDict
        elif args['datatype'] == 'json':
            data = request.get_json()
            print('json data:', data) # ImmutableMultiDict
            v = data.get('key1')
            print('json key1:', v) # ImmutableMultiDict




    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
