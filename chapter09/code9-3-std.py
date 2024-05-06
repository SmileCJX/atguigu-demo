import random
# 随机小数
a = random.random()
print(a)
# 随机整数
a = random.randint(1, 100)
print(a)

# 获取列表中的随机元素
list1 = [1, 2, 3, 4, 5, 6]
print(list1[random.randint(0, len(list1) - 1)])

print(random.choice(list1))
print(random.choice('hello'))

print(ord('A'))
n = 5
# 生成一个随机字母组成的列表
a = []
for i in range(20):
    s = ''
    for j in range(n):
        t = random.randint(65, 90)
        s += chr(t)
    a.append(s)
print(a)