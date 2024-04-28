# 类型的创建
tuple1 = (1, 2, 3, True, 'hello')
print(tuple1)
print(type(tuple1))

list1 = [1]
print(list1)
tuple2 = (1, ) # 元组里只有一个元素时， 加一个逗号
print(tuple2)
print(type(tuple2))

tuple3 = tuple() # tuple()： 类型转换
print(tuple3)
print(type(tuple3))
tuple4 = ()
print(tuple4)
print(type(tuple4))

tuple5 = tuple('hello') # str --> tuple
print(tuple5)

tuple6 = tuple([1, 2, 3, 4]) # list --> tuple
print(tuple6)