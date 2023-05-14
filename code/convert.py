import pandas as pd
import sqlite3

# 读取 Excel 文件中的所有 sheet
xls_file = 'spy/daily.xlsx'
xls_data = pd.read_excel(xls_file, sheet_name=None)

# 连接到 SQLite 数据库
conn = sqlite3.connect('daily.db')

# 遍历每个 sheet 并将数据导入 SQLite 数据库
for sheet_name, sheet_data in xls_data.items():
    # 将数据导入 SQLite 数据库
    sheet_data.to_sql(sheet_name, conn, if_exists='replace', index=False)

# 关闭数据库连接
conn.close()
