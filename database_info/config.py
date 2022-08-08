# coding=UTF-8
from database_info import conMysql


class Config:
    root, password, coninfo = conMysql.connect()
    sql = 'mysql+pymysql://' + root + ':' + password + '@' + coninfo + ':3306/stuinfo?charset=utf8'
    SQLALCHEMY_DATABASE_URI = sql
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_KEY = 'jisuanjixueyuan'

