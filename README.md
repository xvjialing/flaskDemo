# flask

- 最简单实例
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

#### 运行方式

1. 用flask命令运行
```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

2. 用python -m flask运行

```
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```

3. 公网访问

```
flask run --host=0.0.0.0
```

4. 调试模式运行

```
$ export FLASK_DEBUG=1
$ flask run
```
#### 路由（Route）
1. route()函数用来绑定一个指向url的函数

```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

2. 变量规则

要将变量部分添加到URL，可以将这些特殊部分标记为<variable_name>。然后将这个标记作为关键字参数传递给函数。通过使用<converter：variable_name>指定规则来使用转换器。

```
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

可用的转换器（converter）

| 类型        | 描述           |
| ------------- |:-------------:|
| string      | 接受任何没有斜杠的文本（默认类型） | 
| int      | 接收integer类型      |
| float | 接收float类型      |
| path | 像默认类型，但也接受斜线      |
| any | 匹配提供的项目之一      |
| uuid | 接受UUID字符串      |


