class Player(object): # 父类
    numbers = 0 # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    def __init__(self, name, age, city, level):  # 初始化函数(构造函数)
        self._name = name # 实例属性
        self._age = age
        self._city = city
        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level
        Player.numbers += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == self._name:  # 使用 self._name 访问实例变量
            raise ValueError('修改的名字与现在的名字相同，请重新修改')
        else:
            self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise Exception('年龄必须是整数')
        if age < 0 or age > 100:
            raise Exception('年龄必须在0到100之间')
        self._age = age

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if len(city) > 10 or len(city) < 2:
            raise Exception('城市名称有误， 请检查！')
        self._city = city
    def show(self): # 创建实例方法
        print('我是荣耀王振的第%d个玩家，我的名字是%s， 我来自%s, 我的段位是%s' % (Player.numbers, self.name, self.city, self.level))

    def level_up(self):
        index1 = Player.levels.index(self.level)
        if index1 < len(Player.levels) - 1:
            self.level = Player.levels[index1 + 1]

    def get_weapon(self, weapon):
        self.weapon = weapon

    def show_weapon(self):
        return self.weapon.show_weapon()

    @classmethod
    def get_players(cls): # 类方法
        print('荣耀王者的用户数据已经达到了%d人' % cls.numbers)

    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age'] > 18:
            return True
        else:
            return False

cjx = Player('cjx', 26, '山东', '王者')
cjx.name = 'tom'
print(cjx.name)
# cjx.name = 'tom'
# print(cjx.name)

cjx.age = 22
# cjx.age = 102
print(cjx.age)

cjx.city = '宿州'
print(cjx.city)