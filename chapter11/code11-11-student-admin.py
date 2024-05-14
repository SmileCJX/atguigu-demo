'''
需求：学生管理系统

学生

老师

班级

课程
'''
class User(object):
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    def show_infos(self): # 显示学生信息用的
        print('*' * 30)
        print('姓名：%s' % self.name)
        print('年龄：%d' % self.age)
        print('性别：%s' % self.gender)
        print('学(工)号：%d' % self.id_number)
        print('*' * 30)


class Student(object):
    # 属性：姓名、年龄、性别、学号
    def __init__(self, name, age, gender, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    def show_infos(self): # 显示学生信息用的
        print('*' * 30)
        print('姓名：%s' % self.name)
        print('年龄：%d' % self.age)
        print('性别：%s' % self.gender)
        print('学(工)号：%d' % self.id_number)
        print('*' * 30)

class Teacher(object):
    # 属性： 姓名、年龄、性别、工号、是否是导员、班级列表

    pass

class Cla(object):
    pass

class Course(object):
    pass

cjx = User('cjx', 20, '男', 1)
cjx.show_infos()

