# 转换为整数int
# 字符串str-->整数int
# 纯数字的字符串，不然会报错
s = '2024'
print(s)
n = int(s)
print(n)
print(type(s), type(n))

# 浮点数floot-》整数int
s1 = 2.23
print(int(s1))
# 布尔bool——》整数int
s2, s3 = True, False
print(int(s2), int(s3))

# 转换为浮点数floot
# str ——》float
s = '426.5' # 有没有小数点都可以
print(float(s))
n = 2024
print(float(n))
# bool -> float
print(float(s2), float(s3))

# 转换为布尔bool
s = '0'
print(bool(s))
s1 = ''
print(bool(s1))

n = 1
print(bool(n))

# float -> boool
s1 = '   '
print(bool(s1))

# 转换为字符串str
# int -> str
n = 5
print(type(str(n)))
# float
f = 5.3
print(str(f))
print((type(str(f))))

a = True
print(str(a))
print(type(str(a)))

# 进制的转换
s = '10'
print(int(s))
print(int(s, 2))
s = '1a'
print((int(s, 16)))

c = 300
print(id(c))