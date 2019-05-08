# @Time   : 2019-05-08
# @Author : zhangxinhao
from flask import Flask, jsonify, request
app = Flask(__name__)
from flask_mako import render_template, MakoTemplates

mako = MakoTemplates()
mako.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', abc='hello world', x=5)

@app.route('/login')
def login():
    return render_template('login.html', a=True)

@app.route('/form')
def form():
    return render_template('form.html', a=True)

@app.route('/sss')
def sss():
    print(request.full_path)
    return render_template('index.html', abc='hello world', x=5)

print('xxx')

if __name__ == '__main__':
    app.run(debug=True)

