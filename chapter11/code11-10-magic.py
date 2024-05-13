class User(object):
    def __init__(self, name):
        print('__init__被调用')
        self.name = name

    def __str__(self):
        return '我的名字是%s' % self.name

    def __add__(self, other):
        return self.name + other.name

    def __eq__(self, other):
        return self.name == other.name

cjx = User('cjx')
print(str([1, 2, 3]), type(str([1, 2, 3])))
print(str(cjx))
print(cjx)

print(1 + 3)
print('hi' + 'cjx')
jack = User('jack')
jack.name = 'cjx'
print(cjx + jack)

print(6 ==  7)
print(cjx == jack)