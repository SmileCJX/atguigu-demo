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


class Student(User):
    # 属性：姓名、年龄、性别、学号
    def __init__(self, name, age, gender, id_number):
        super().__init__(name, age, gender, id_number)

    def show_infos(self): # 显示学生信息用的
        super().show_infos()

class Teacher(User):
    # 属性： 姓名、年龄、性别、工号、是否是导员、班级列表
    def __init__(self, name ,age, gender, id_number, dao, cla):
        super().__init__(name, age, gender, id_number, )
        self.dao = dao
        self.cla = cla
    def show_infos(self):
        super().show_infos()
        print('是否是导员：%s' % ['否', '是'][self.dao])
        print('辅导班级：')
        if not self.cla:
            print('空')
        else:
            for i in self.cla:
                print(i)
        print('*' * 30)

class Cla(object):
    # 属性： 班级名称、班级号、辅导员、学生
    def __init__(self, name, id_number, teacher, students):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students

    def show_infos(self):
        print('*' * 15 + '班级信息' + '*' * 15)
        print('班级名称：%s' % self.name)
        print('班级班号：%d' % self.id_number)
        print('辅导员：%s' % self.teacher.name)
        print('学生信息：')
        if not self.students:
            print('空')
        else:
            for i in self.students:
                print(i.name)
        print('*' * 15 + '班级信息' + '*' * 15)


    def add_students(self, student): # 增加学生
        if student in self.students:
            raise Exception('此学生已经进班，不允许重复操作！')
        else:
            self.students.append(student)
        return True
    def sub_student(self, student): # 减少学生
        if student in self.students:
            self.students.remove(student)
            return True
        else:
            raise Exception('此学生不在班级！')
class Course(object):
    pass

cjx = Student('cjx', 20, '男', 1)
rose = Student('rose', 21, '女', 2)
cjx.show_infos()

jack = Teacher('jack', 50, '男', 5, False, [])
jack.show_infos()

tom = Teacher('tom', 50, '男', 53, True, ['计算机二班', '法律三班'])
tom.show_infos()

computer_2 = Cla('计算机二班', 1002, tom, [])
computer_2.show_infos()

computer_1 = Cla('计算机一班', 1001, tom, [cjx])
computer_1.show_infos()

computer_2.add_students(rose)
computer_2.show_infos()

# computer_2.sub_student(rose)
# computer_2.show_infos()

# computer_2.sub_student(rose)
computer_2.add_students(rose)