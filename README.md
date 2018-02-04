# myproject

a tiny movie-blog flask project

features:
login/register
show movies and comments/document


2018/2/1  更新：
为项目增加shell指令： db  migrate

2018/2/2 - 2018/2/3
为model类增加save subbmit put方法

2018/2/4
为自定制的model类增加__json__()方法
使jsonify中可以直接添加model类的对象

在api/__init__中自定义ApiView(继承自FlaskView),并使api中的view函数继承
ApiView  其中改写了proxy函数,如果传入的response类型为MyModel类型就可以直接
jsonify   即api的view函数中可以直接返回model对象








