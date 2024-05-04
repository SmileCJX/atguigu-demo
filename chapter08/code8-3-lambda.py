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

print('*' * 30)
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
result = filter(lambda x:x != 0, a)
print(list(result))

result = 0
mul = 1
for i in a[::-1]:
    result = result + i * mul
    mul = mul * 10 ** len((str(i)))
print(result)

# 在这个特定的上下文中，lambda函数是作为reduce函数的参数传递的。在Python中，reduce函数接受一个函数（通常是lambda函数）和一个可迭代对象作为参数，然后将该函数应用于可迭代对象的所有元素，以产生单个结果。
#
# 在lambda函数中，第一个参数（通常用x表示）是reduce函数中的累积值，它随着每次迭代更新。第二个参数（通常用y表示）是可迭代对象中的当前元素。在每次迭代中，lambda函数将累积值（x）和当前元素（y）作为输入，执行指定的操作，并返回新的累积值，以便用于下一次迭代。这种命名约定是为了与reduce函数的预期行为相匹配，使得代码更易于理解。
result = reduce(lambda x, y:x * 10 ** len(str(y)) + y, a)
print(result)


