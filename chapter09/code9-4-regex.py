import re
result = re.match('hello', 'hello world')
print(result)

# \d：检测字符串是否为纯数字的字符串
result = re.match(r'\d+', '12343334345')
print(result)

# \w：数字字母下划线
result = re.match(r'\w+', 'a*8')
print(result)

# \s：空白字符
result = re.match(r'\s+$', '  tre')
print(result)
# .: 任意字符
result = re.match(r'^code\d-\d-\w+$', 'code9-4-regex')
print(result)

# [] 区间，可选列表
result = re.match(r'^[abcd]+$', 'abbcd')
print(result)

# |: 或
result = re.match(r'a|b|c', 'ba')
print(result)