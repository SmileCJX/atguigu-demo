# import pandas as pd
#
# # 读取Excel文件
# file_path = '/Users/caijunxiang/IdeaProjects/python/atguigu-demo/work/index-script.xlsx'  # 替换为你的文件路径
# df = pd.read_excel(file_path, header=None, skiprows=1)  # 跳过第一行（标题行）
#
# # 生成SQL语句
# sql_statements = []
#
# for index, row in df.iterrows():
#     table_name = row[0]  # 表名
#     primary_key_id = row[1]  # 主键ID
#
#     # 创建索引的SQL语句
#     sql_statements.append(f"CREATE UNIQUE INDEX IDX_ODS_{table_name}_{primary_key_id} ON DAM_DW.ODS_{table_name}({primary_key_id}) ONLINE;")
#     sql_statements.append(f"CREATE INDEX IDX_ODS_{table_name}_ODS_ETL_UPDATE_TIME ON DAM_DW.ODS_{table_name}(ODS_ETL_UPDATE_TIME) ONLINE;")
#     sql_statements.append(f"CREATE INDEX IDX_ODS_{table_name}_ODS_BIZ_TIME ON DAM_DW.ODS_{table_name}(ODS_BIZ_TIME) ONLINE;")
#     sql_statements.append(f"CREATE UNIQUE INDEX IDX_DWS_{table_name}_CHARGE_PROJ_ID ON DAM_DW.DWS_{table_name}({primary_key_id}) ONLINE;")
#     sql_statements.append(f"CREATE INDEX IDX_{table_name}_DWS_ETL_UPDATE_TIME ON DAM_DW.DWS_{table_name}(DWS_ETL_UPDATE_TIME) ONLINE;")
#     sql_statements.append(f"CREATE INDEX IDX_{table_name}_DWS_BIZ_TIME ON DAM_DW.DWS_{table_name}(DWS_BIZ_TIME) ONLINE;")
#
# # 写入SQL文件
# with open('indexes.sql', 'w') as file:
#     file.write('\n'.join(sql_statements))
#
# print("SQL文件生成完毕：indexes.sql")





import pandas as pd

# 读取Excel文件
file_path = '/doc/index-script.xlsx'  # 替换为你的文件路径
df = pd.read_excel(file_path, header=None, skiprows=1)  # 跳过第一行（标题行）

# 生成SQL语句
sql_statements = []

for index, row in df.iterrows():
    table_name = row[0]  # 表名
    primary_keys = row[1]  # 主键ID，可能包含多个，以顿号分隔

    # 替换顿号为下划线
    primary_keys = primary_keys.replace('、', '，')

    # 通过逗号分隔主键ID
    primary_key_list = primary_keys.split(',')

    # 确保去掉任何多余的空白字符
    primary_key_list = [key.strip() for key in primary_key_list]

    # 创建索引的SQL语句
    sql_statements.append(f"CREATE UNIQUE INDEX IDX_ODS_{table_name}_{'_'.join(primary_key_list)} ON DAM_DW.ODS_{table_name}({', '.join(primary_key_list)}) ONLINE;")
    sql_statements.append(f"CREATE INDEX IDX_ODS_{table_name}_ODS_ETL_UPDATE_TIME ON DAM_DW.ODS_{table_name}(ODS_ETL_UPDATE_TIME) ONLINE;")
    sql_statements.append(f"CREATE INDEX IDX_ODS_{table_name}_ODS_BIZ_TIME ON DAM_DW.ODS_{table_name}(ODS_BIZ_TIME) ONLINE;")
    sql_statements.append(f"CREATE UNIQUE INDEX IDX_DWS_{table_name}_{'_'.join(primary_key_list)} ON DAM_DW.DWS_{table_name}({', '.join(primary_key_list)}) ONLINE;")
    sql_statements.append(f"CREATE INDEX IDX_{table_name}_DWS_ETL_UPDATE_TIME ON DAM_DW.DWS_{table_name}(DWS_ETL_UPDATE_TIME) ONLINE;")
    sql_statements.append(f"CREATE INDEX IDX_{table_name}_DWS_BIZ_TIME ON DAM_DW.DWS_{table_name}(DWS_BIZ_TIME) ONLINE;")

# 写入SQL文件
with open('../doc/indexes.sql', 'w') as file:
    file.write('\n'.join(sql_statements))

print("SQL文件生成完毕：indexes.sql")


