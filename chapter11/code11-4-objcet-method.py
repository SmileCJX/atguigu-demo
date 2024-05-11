class Player(object):
    numbers = 0 # 类属性
    def __init__(self, name, age, city):  # 初始化函数(构造函数)
        self.name = name # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1

    def show(self): # 创建实例方法
        print('我是荣耀王振的第%d个玩家，我的名字是%s， 我来自%s' % (Player.numbers, self.name, self.city))

cjx = Player('cjx', 24, '大连')
cjx.show()

