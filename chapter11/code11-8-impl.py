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


def speak(object): # animal
    object.speak()


animal = Animal()
animal.speak()
speak(animal)

kitty = Cat()
putty = Dog()
speak(kitty)
speak(putty)
# kitty.speak()
# putty.speak()