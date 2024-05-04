def f(a, b):
    return a + b

result = f(1, 2)
print(result)

fun = lambda a,b:a + b
result = fun(1, 2)
print(result)

a = [1, 2, 3, 4, 5]
b = []
for i in range(len(a)):
    a[i] = a[i] ** 2
print(a)


a = [1, 2, 3, 4, 5]
result = map(lambda x:x ** 3, a) # 映射
print(list(result))

# reduce 规约
from functools import reduce
result = reduce(lambda x, y: x + y, a)
print(result)

result = 1
a = [1, 2, 3, 4, 5]
for i in a:
    result *= i
print(result)

# filter 过滤
# for i in a:
#     if a % 2 == 0:
#         b.append(i)

a = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2, a)
print(list(result))

a = [1, 2, 3, 40, 5, 6, 0, 6, 0, 5]
result = filter()
