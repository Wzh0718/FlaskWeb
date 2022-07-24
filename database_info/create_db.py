# coding=UTF-8
from database_info.model import Admin
from sqlalchemy.schema import CreateTable

print(CreateTable(Admin.__table__))
