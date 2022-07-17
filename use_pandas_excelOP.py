# -*- coding: UTF-8 -*-
"""
@File: use_pandas_excelOP.py
@Description: 使用pandas操作excel
@Author: lee sure
@DateTime: 2021/12/09 00:29
@Project_name: pythonProject
@IDE: PyCharm
"""

import pandas as pd
from openpyxl import load_workbook

data= pd.read_excel("op_excel.xlsx",sheet_name=1)
# 读取后drop
mydata = data.drop([1,3], axis=0)
# 保存新的数据
book = load_workbook('data.xlsx')
writer = pd.ExcelWriter('data.xlsx',engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
mydata.to_excel(writer, "mysheet")
writer.save()
