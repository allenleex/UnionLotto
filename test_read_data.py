import pandas as pd
from pyecharts.charts import *

# 读取表格数据
data = pd.read_csv('data.csv', encoding='utf-8', engine='python')
print(data.to_string())

