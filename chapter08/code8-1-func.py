def f():
    print('python')


f()

def sum_2(a, b): # 形式参数
    return a + b

result = sum_2(6, 9) # 实际参数
# a = len('get')
# print(a)
# print(result)

def power(x, n = 2): # n: 默认参数，缺省参数
    return x ** n

a = power(4, 3)
b = power(5, 3)
c = power(6)
print(a)
print(b)
print(c)
a = int('16', 8)
print(a)

def infos(name, age = 24, gender = '女'):
    return '大家好，我叫%s， 我今年%d岁，我是一名%s生' % (name, age, gender)


s = infos('cjx', 30, '男')
lily = infos('lily', 25)
jack = infos('jack', 30, '男')
jack = infos('jack', gender='男')
print(s)
print(jack)

# 可变参数
def total(*a): # 可变参数
    result = 0
    for i in a:
        result +=i
    return result

result = total([1, 4, 5, 6, 7, 8, 3])
print(result)
