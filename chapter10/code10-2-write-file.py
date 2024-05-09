# 打开文件
f = open('test.txt', mode='w', encoding='utf-8')
# 写入文件内容
f.write('你好，我是cjx\n')
f.write('你是谁\n')
context = ['你好，我是cjx', '你是谁']
for i in context:
    f.write(i + '\n')

# 关闭文件
f.close()