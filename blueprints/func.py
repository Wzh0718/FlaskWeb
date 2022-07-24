# coding=UTF-8
from flask import Blueprint, render_template, request, flash, redirect
from sqlalchemy import create_engine

bp = Blueprint("func", __name__, url_prefix='/func')


@bp.route("/1", methods=['GET', 'POST'])
def func1():
    if request.method == 'POST':
        idcard = request.form['idcard']
        print(idcard)
        if idcard != "":
            # 查询语句
            sql = create_engine("mysql+pymysql://root:123456@localhost:3306/stuinfo_1")
            stuinfos = sql.execute(f'select * from student where 身份证号="{idcard}";').fetchone()
            if stuinfos is None:
                flash('查询不到，请重新输入')
            return render_template("func1.html", stuinfos=stuinfos)
        else:
            # print(request.remote_addr+" "+request.remote_user)
            return redirect('1')
    return render_template("func1.html")



