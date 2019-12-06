class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Husky(Dog):
    pass

def run_twice(animal):
    animal.run()

if __name__ == '__main__':
    mydog = Dog()
    mydog.run()
    mycat = Cat()
    mycat.run()
    a = list()
    b = Dog()
    c = Cat()
    aa=isinstance(a,list)
    bb=isinstance(b,Dog)
    cc=isinstance(c,Cat)
    dd=isinstance(c,Animal)
    print(aa)
    print(bb)
    print(cc)
    print(dd)


    run_twice(Animal())
    run_twice(Dog())
    run_twice(c)