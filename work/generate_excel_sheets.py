"""
从Excel模板的指定列（C2:C15）提取名称，生成新Excel文件的工作表。
输入文件：字段对照清单.xlsx
输出文件：新文件.xlsx
"""
import pandas as pd

# 读取Excel文件
df = pd.read_excel('字段对照清单.xlsx', sheet_name='目录')

# 获取C2到C15的名称作为新tab的标题，并修正不合法字符
tab_titles = df.iloc[1:15, 2].str.replace('/', '-').tolist()
print(tab_titles)

# 创建一个新的Excel文件
writer = pd.ExcelWriter('新文件.xlsx')

# 遍历每个tab标题，并在新文件中创建对应的空工作表
for title in tab_titles:
    # 创建一个空的DataFrame
    empty_df = pd.DataFrame()
    # 将空DataFrame写入新文件的对应tab，使用title作为工作表的名称
    empty_df.to_excel(writer, sheet_name=title, index=False)

# 保存并关闭新文件
writer._save()
