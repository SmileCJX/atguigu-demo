class Player(object):
    def __init__(self, name, age, city):  # 初始化函数(构造函数)
        self.name = name
        self.age = age
        self.city = city

# 实例的属性
cjx = Player('cjx', 24, '上海')
cjx.city = '杭州'
print(cjx.name, cjx.age, cjx.city)
tom = Player('tom', 34, '重庆')
print(tom.name, tom.age, tom.city)
tom.height = 100
tom.age = 32
print(tom.__dict__, type(tom.__dict__)) # 获取实例（对象）的所有属性


# 武器： 名字 攻击值 等级
class weapon(object):
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

gun = weapon('magic', 1000, 3)
print(gun.__dict__)