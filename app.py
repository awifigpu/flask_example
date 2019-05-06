# @Time   : 2019-04-16
# @Author : zhangxinhao
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/<db_id>')
def get_db(db_id):
    # db_id = int(db_id)
    return jsonify({
        'db_id': db_id,
        'person_ids': ["%s-%d" % (db_id, i) for i in range(10)]
    })


@app.route('/<db_id>/<person_id>')
def get_person(db_id, person_id):
    # db_id = int(db_id)
    return jsonify({
        'db_id': db_id,
        'person_id': person_id,
        'img_ids': ["%s-%s-%d" % (db_id, person_id, i) for i in range(10)]
    })


@app.route('/<db_id>', methods=['POST', 'GET'])
def create_person(db_id):
    print(request.json)
    
    return jsonify({'code':0})







if __name__ == '__main__':
    app.run()
