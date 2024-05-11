class Player(object):
    def __init__(self, name, age, city):  # 初始化函数
        self.name = name
        self.age = age
        self.city = city

# 实例的属性
cjx = Player('cjx', 24, '上海')
print(cjx.name, cjx.age, cjx.city)
tom = Player('tom', 34, '重庆')
print(tom.name, tom.age, tom.city)