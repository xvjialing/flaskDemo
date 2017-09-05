from flask import Flask,request,session,redirect,url_for,abort
from flask import render_template
from flask import request
import config

from flask_sqlalchemy import SQLAlchemy

# 初始化flask对象
# Flask
# 需要传递一个参数__name__
# 1.方便flask框架寻找资源
# 2. 方便flask插件比如Flask-SQLAlchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)
app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:xjl1994920@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)


#@app.route()是一个装饰器
#@开头，并且在函数上上面，说明是装饰器
#这个装饰器的作用是视图与URL的映射
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do login"
    else:
        return "show login form "

@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)


#如果当前文件作为入口文件运行，那么就执行app.run()
if __name__ == "__main__":
    app.run()
#app.run()
#启动一个应用服务器
#while True
#   listen()
