import os
import pandas as pd

# 设置文件夹路径
folder_path = '/Users/caijunxiang/Documents/项目文件/02-数据采集/'

# 初始化总行数计数器
total_rows = 0

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件扩展名是否为xlsx或xls
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        # 读取Excel文件
        try:
            df = pd.read_excel(file_path)
            # 累加数据行数
            total_rows += df.shape[0]
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# 打印总行数
print(f"Total number of rows: {total_rows}")