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

# 身份证号
result = re.match(r'^\d{6}((20[012][01234)])|(1[89]\d\d))\d{7}([\dX])$', '350123199601190328')
print(result)


from my_package import my_tools
# 手机号码
# result = re.match(r'^1\d{10}$', '12345678911')
print(my_tools.is_phone_number('123456789111'))
print(my_tools.is_id_number('3501231996101190328'))