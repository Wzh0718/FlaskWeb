# coding=UTF-8
from sqlalchemy import Column, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    __tablename__ = 'admin'
    username = Column(String(80), primary_key=True)
    password = Column(String(160))

    def __int__(self, username, password):
        self.username = username
        self.password = password
    #
    # def get_id(self):
    #     return self.username
    #
    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return True
