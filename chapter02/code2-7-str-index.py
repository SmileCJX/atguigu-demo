# 创建字符串
s = 'hello,world'
print(s[0])
print(s[4])
print(s[-1])
# 切片 变量名【起始索引：结束索引+1：步数】
# 步数默认为1，可省略不写
# 起始索引默认为0，可省略不写
# 结束索引默认为-1，可省略不写
print(s[0:2])  # 包头不包尾
print(s[6:9])  # wor
print(s[0:9:2])

s2 = '123456789'
print(s2[0:9:2])
print(s2[:9:2])
print(s2[::2])
print(s2[::3])

# 字符串反转
print(s2[-1:-10:-1])
print(s2[::-1])