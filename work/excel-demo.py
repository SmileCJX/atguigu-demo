import pandas as pd

# 读取Excel文件，生成注释内容
# /Users/caijunxiang/Documents/厦门市易联众易惠科技有限公司/【01】部门资料/【06】部门规划/售前支持/【39】辽宁省智慧化管理平台/项目文件/02-数据采集
df = pd.read_excel('/Users/caijunxiang/Documents/厦门市易联众易惠科技有限公司/【01】部门资料/【06】部门规划/售前支持/【39】辽宁省智慧化管理平台/项目文件/02-数据采集/1.1-患者基本信息数据表-PERSONALINFORMATION.xlsx', sheet_name='定义')

tab_titles = df.iloc[0:81, 2].str.replace('/', '-').tolist()
print(tab_titles)

column_titles2 = df.iloc[0:81, 3].str.replace('/', '-').tolist()
column_titles2_lower = [title.lower() for title in column_titles2]
print(column_titles2_lower)


tab_titles2 = df.iloc[0:81, 7].str.replace('/', '-').tolist()
print(tab_titles2)

# COMMENT ON COLUMN personalinformation.personal_id IS '患者唯一ID号，联合主键之一';

# 使用 zip 函数将两个列表的元素配对，并使用列表推导式拼接每个配对的元素
# comment_list = [f"{title1}; {title2}" for title1, title2 in zip(tab_titles, tab_titles2)]
comment_list = [f"COMMENT ON COLUMN personalinformation.{column} IS '{title1}; {title2}';" for column, title1, title2 in zip(column_titles2_lower, tab_titles, tab_titles2)]
# 打印结果
for i in comment_list:
    print(i.replace(' nan', ''))

# 去除nan