class Player(object):
    numbers = 0 # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    def __init__(self, name, age, city, level):  # 初始化函数(构造函数)
        self.name = name # 实例属性
        self.age = age
        self.city = city
        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level
        Player.numbers += 1

    def show(self): # 创建实例方法
        print('我是荣耀王振的第%d个玩家，我的名字是%s， 我来自%s, 我的段位是%s' % (Player.numbers, self.name, self.city, self.level))

    def level_up(self):
        index1 = Player.levels.index(self.level)
        if index1 < len(Player.levels) - 1:
            self.level = Player.levels[index1 + 1]


cjx = Player('cjx', 24, '大连', '青铜')
cjx.show()
cjx.level_up()
cjx.show()
cjx.level_up()
cjx.show()
cjx.level_up()
cjx.show()
cjx.level_up()
cjx.show()
cjx.level_up()
cjx.show()

