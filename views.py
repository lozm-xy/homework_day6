from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify

from forms import loginForm

blue = Blueprint('blue',__name__)

#第一题
@blue.route('/gologin',methods=['get','post'])
def gologin():
    loginform = loginForm()
    #if form.validate_on_submit()  #此语句可以直接判断是否提交或验证，就不需要下面的if语句判断了
        #username = loginform.username.data
        #if loginform.username.data=='tom' and request.form.get('password')=='123456':
            #session['username'] = username  #用户名密码正确，在session中设置属性
            #return redirect(url_for('blue.success'))
    if loginform.username.data and loginform.password.data:
        if loginform.username.data=='tom' and request.form.get('password')=='123456':
            return redirect(url_for('blue.success'))
        else:
            flash('用户名或密码错误')
            return render_template('gologin.html',loginform=loginform)
    else:
        return render_template('gologin.html',loginform=loginform)

@blue.route('/login')
def success():
    return "<h3 style='color:red'>恭喜，登录成功！</h3>"

#第二题
@blue.route('/')
def gosearch():
    return render_template('showinfo.html',msg='')
@blue.route('/search',methods=['get','post'])
def search():
    # if request.form.get('choice') == 'fruit':
    fruit_info = {'name':('苹果','橙子','火龙果','香蕉','葡萄','西瓜','草莓'),'price':(12.5,15,48,10,16,14,20)}
    return jsonify(fruit_info)
    # elif request.form.get('choice') == 'sport':
    #     sport_info = ['篮球','乒乓球','羽毛球','足球','网球','排球']
    #     return render_template('showinfo.html',msg = sport_info)


#第三题
@blue.route('/showimage')
def show():
    return render_template('showimage.html')


