# coding=UTF-8
from datetime import timedelta

from flask import Flask, render_template, session
from blueprints import login_bp
from blueprints import func_bp
from blueprints import admin_bp
from database_info.config import Config
from database_info.model import db
import logging

# from flask_login import LoginManager, login_required

app = Flask(__name__)
app.secret_key = 'jisuanjixueyuan'
# 倒入数据库信息
app.config.from_object(Config)
db.init_app(app)
db.create_all(app=app)

app.register_blueprint(login_bp)
app.register_blueprint(func_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    handler = logging.FileHandler('log/flask.log', encoding="UTF_8")
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run()
