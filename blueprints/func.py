# coding=UTF-8
from flask import Blueprint, render_template, request, flash, redirect
from sqlalchemy import create_engine
from flask import current_app
from database_info import conMysql
import re

bp = Blueprint("func", __name__, url_prefix='/func')


@bp.route("/1", methods=['GET', 'POST'])
def func1():
    if request.method == 'POST':
        idcard = request.form['idcard']
        if idcard != "":
            # 查询语句
            r = r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
            if re.findall(r, idcard):
                root, password, coninfo = conMysql.connect()
                sql_connect = 'mysql+pymysql://' + root + ':' + password + '@' + coninfo + ':3306/stuinfo_1?charset=utf8'
                sql = create_engine(sql_connect)
                stuinfos = sql.execute(f'select * from student where 身份证号="{idcard}";').fetchone()
                if stuinfos is None:
                    flash('查询不到，请重新输入')
                return render_template("func1.html", stuinfos=stuinfos)
            else:
                flash('身份证号码格式错误')
                try:
                    current_app.logger.warning('A warning ip is', request.headers['X-real-ip'])
                except:
                    current_app.logger.warning('A warning ip is', request.remote_addr)
                return redirect('1')
        else:
            flash('身份证不能为空')
            try:
                current_app.logger.warning('A warning ip is', request.headers['X-real-ip'])
            except:
                current_app.logger.warning('A warning ip is', request.remote_addr)
            return redirect('1')
    return render_template("func1.html")
