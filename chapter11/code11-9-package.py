# 封装
class User(object):
    def __init__(self, name, age):
        self._name = name # 受保护的变量
        self.__age = age # 私有变量

    '''
    把函数当做变量去使用
    @property
    def 变量名（）# 获取变量
    @age.setter
    def 变量名()#修改变量
    '''

    @property
    def age(self):
        return self.__age

    # @age.setter #变量的修改器
    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise Exception('年龄只能是整数')
    def show_infos(self):
        print('大家好， 我是%s， 我今年%d' % (self._name, self.__age))

cjx = User('cjx', 24)
print(cjx.age)
cjx.age = 25
print(cjx.age)
# print(cjx.get_age())
# cjx.set_age(25)
# cjx.set_age('二十五')
# print(cjx.get_age())

# print(cjx._name)
# print(cjx.__age) # 私有变量无法打印
# cjx._show_infos()
# print(dir(cjx))
# print(cjx.__dict__)
# print(cjx._User__show_infos())
# print(cjx._User__age) # 可以通过dict得到
# cjx.name = 'Tom'
# cjx.age = 25
# print(cjx.name)
# print(cjx.age)