# 全局变量
num1 = 10 # 不可变数据类型
list1 = [1, 2, 3, 4, 5] # 可变数据类型

def f():
    global num1 # 声明在f中使用的num1是全局变量num1
    num2 = 20
    num1 = 20 # 这个是重新定义的，会覆盖掉全局变量的值，除非用了num1
    list1[2] = 8
    print('在函数f中打印num1的值', num1)
    print('在函数f中打印list1的值', list1)
    print('num2的值', num2)
print('num1的值', num1)
f()
# print('在函数f外打印变量num2的值', num2) #局部变量不能在函数外使用
print('在函数f执行后打印num1的值', num1)
print(list1)

