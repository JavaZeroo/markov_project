import pandas as pd
import pyproj

def convert_coordinates(easting, northing):
    bng = pyproj.Proj(init='epsg:27700')
    wgs84 = pyproj.Proj(init='epsg:4326')
    lon, lat = pyproj.transform(bng, wgs84, easting, northing)
    return lat, lon

# 读取示例表格数据
df = pd.read_csv('data/Book2.csv')  # 替换成您的文件名

# 创建新的经纬度列
df['Latitude'] = 0.0
df['Longitude'] = 0.0

# 遍历每行数据进行坐标转换
from tqdm import tqdm
for index, row in tqdm(df.iterrows()):
    easting = row['STATION_EASTING']
    northing = row['STATION_NORTHING']
    latitude, longitude = convert_coordinates(easting, northing)
    df.at[index, 'Latitude'] = latitude
    df.at[index, 'Longitude'] = longitude

# 打印转换后的表格
df.to_csv('data/Book2_converted.csv', index=False)