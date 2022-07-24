# coding=UTF-8
import time, os

from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from database_info.dataInput import DataProcessing
from database_info.model import db

bp = Blueprint("admin", __name__, url_prefix='/admin')


# 伪基站
@bp.route('/test/number/session')
def find():
    usrname_list = db.session.execute("select username from admin")
    password_list = db.session.execute("select password from admin")
    check_username = ''
    check_password = ''
    for i in usrname_list:
        check_username = i[0]
    for i in password_list:
        check_password = i[0]
    return check_username, check_password


# 登陆
@bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        usrname = request.form['username']
        password = request.form['password']
        check_username, check_password = find()
        #     检测站点
        if usrname == "" or password == "":
            flash("不能为空")
            return redirect('login')
        if usrname != check_username or password != check_password:
            flash("输入错误")
            return redirect('login')
        session['username'] = check_username
        return redirect('index')
    return render_template('admin/func2.html')


# 主页
@bp.route('/index', methods=['GET', 'POST'])
def admin_index():
    check_username, check_password = find()
    if session.get('username') != check_username:
        return redirect('login')
    if request.method == 'POST':
        file = request.files.get("info")
        if not file:
            flash("请提交文件")
            return redirect('index')
        upload_folder = './data/'
        # 命名 --> xx.xx.xlsx
        file_name = str(time.time()) + "." + file.filename.split(".")[1]
        file_dir = os.path.join(os.getcwd(), upload_folder)
        file_path = os.path.join(file_dir, file_name)
        file.save(file_path)
        # 路径
        file_path_all = "./data/" + file_name
        # 倒入数据库
        data = DataProcessing(file_path_all)
        if data == {}:
            message = {}
            flash("导入成功")
        else:
            flash("以下同学的数据，不符合要求")
            message = data
            # message = []
            # for i in data:
            #     print(data[i])
            #     message += str(i)+":"+str(data[i])
            # print(message)
        return render_template('admin/index.html', message=message)
    return render_template('admin/index.html')
