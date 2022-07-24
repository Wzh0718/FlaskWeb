# coding=UTF-8
from flask import Blueprint, render_template


bp = Blueprint("qa", __name__, url_prefix='/')


@bp.route("/", methods=['GET', 'POST'])
# @bp.route('/')
def hello_world():  # put application's code here
    return render_template("func1.html")