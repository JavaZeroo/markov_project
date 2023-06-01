import pandas as pd
import sqlite3

# 读取 Excel 文件中的所有 sheet
# xls_file = 'spy/daily.xlsx'
# xls_data = pd.read_excel(xls_file, sheet_name=None)

csv_file = 'data/pp-complete.csv'
csv_data = pd.read_csv(csv_file)
print("finish read")
# 连接到 SQLite 数据库
conn = sqlite3.connect('data/pp-complete.db')

csv_data.to_sql(csv_data, conn, if_exists='replace', index=False)

# 关闭数据库连接
conn.close()
