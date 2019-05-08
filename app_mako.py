# @Time   : 2019-05-08
# @Author : zhangxinhao
from flask import Flask, jsonify, request
from flask_mako import render_template, MakoTemplates
app = Flask(__name__)
mako = MakoTemplates()
mako.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

