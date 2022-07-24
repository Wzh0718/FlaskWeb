# coding=UTF-8
from sqlalchemy import create_engine
import pandas as pd
# pip install xlrd==1.2.0

def DataProcessing(path):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/stuinfo_1?charset=utf8')
    # 数据读取
    data = pd.read_excel(path, sheet_name=0)
    data.drop(["序号", "价格", "学生类型", "分配届别", "分配院系"], axis=1, inplace=True)
    # 去重
    data.drop_duplicates(inplace=True)
    # 去除缺失值
    old_data_len = data.shape[0]
    new_data_len = data.dropna(axis=0).shape[0]
    if old_data_len == new_data_len:
        data.to_sql("student", engine, index=False, if_exists="replace")
        return {}
    else:
        StoreNull = []
        for i, row in enumerate(data.isnull().values):
            if True in row:
                StoreNull.append(i)
        # print("有缺失值的同学：\n", data.loc[StoreNull, ["姓名", "身份证号"]])
        dictNaN = dict(data.loc[StoreNull, ["姓名", "身份证号"]].values)
        data.dropna(axis=0, inplace=True)
        data.to_sql("student", engine, index=False, if_exists="replace")
        return dictNaN

