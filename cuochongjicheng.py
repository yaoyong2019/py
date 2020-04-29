class Animal(object):#动物
    pass
# 大类:
class Mammal(Animal):#哺乳动物
    #print('Animal\n')
    pass
class Bird(Animal):#鸟类
    #print('Animal\n')
    pass
# 各种动物:
# class Dog(Mammal):#狗
#     pass
# class Bat(Mammal):#蝙蝠
#     pass
class Parrot(Bird):#鹦鹉
    pass
class Ostrich(Bird):#鸵鸟
    pass
#功能
class Runnable(object):
    def run(self):
        print('Running......')
class Flyable(object):
    def fly(self):
        print('Flying......')
#继承
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
#shili
myDog = Dog()
myDog.run()
myBat = Bat()
myBat.fly()