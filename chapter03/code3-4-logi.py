# and 与，并且
print(True and False)
print(True and True and False)
print(1 == 1 and False and True)
print('hello' and 'hi') # 短路运算,特别注意
print('' and 'hi')
print(False and 'hi')
print(0 and 1)
# or 或者
print(True or False)
print(1 or 0)
print(2024 or 2025 or 0)
print(0 or '' or 998)
print(0 or '')
# 非not
print(not True)
print(not 1)
print(not '')
print(not 'hello')
# 优先级 not > and > or
print(True and False and not False)
print(True or False and True or False)