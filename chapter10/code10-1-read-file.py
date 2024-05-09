import os
# 打开文件
# f = open('../chapter09/test2.txt') # 相对路径的写法
# f = open('test.txt')
# 绝对路径
path = os.getcwd()
filename = path + '/test.txt'
f = open(filename, mode='r', encoding='utf-8') # 绝对路径

# 读取文件
context = f.read()
print(context)

# 关闭文件
f.close()