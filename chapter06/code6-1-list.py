# 列表的创建
list1 = [] # 空列表
print(list1)
print(type(list1))
list2 = [1, 2, 3, True, False, 'hello']
print(list2)
list3 = list('12345678') # 类型转换，把参数转换成列表
print(list3)

# 列表的索引
print(list3[5])
print(list3[-1])

# 列表的切片
print(list3[2:6:2])

# 列表的加法和乘法
print(list3 + list2)

print(list3 * 3)

# 列表的成员运算
print('0' not in list3)
print('1' in [1, 2, 3, 4])
print([1, 2, 3, 4] < [2, 1]) # 比较第一个字符

# 内置函数
print(len(list3)) # 求元素个数

print(max(list3)) # 求元素的最大值
print(min(list3)) # 求元素的最小值

# del list3
# print(list3)  #删除生效

print('-' * 30)
# 列表的遍历
for i in list3:
    print(i)

for i, j in enumerate(list2):
    print(i,j)

for i in range(len(list2)):
    print(i, list2[i])