# print(len('123'))
# print(len([1, 2, 3, 4, 5]))

class Animal(object):

    def speak(self):
        print('动物的叫声')

class Cat(Animal):

    def speak(self):
        print('喵喵')

class Dog(Animal):

    def speak(self):
        print('汪汪')

class Test(object):

    def speak(self):
        print('test')


def speak(object): # animal
    object.speak()


animal = Animal()
animal.speak()
speak(animal)

kitty = Cat()
putty = Dog()
t = Test()
speak(kitty)
speak(putty)
speak(t)
# kitty.speak()
# putty.speak()