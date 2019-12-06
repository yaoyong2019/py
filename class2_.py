class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
#实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_name(self,name):
        self.__name = name
bart = Student('BOb',89)
bart.print_score()
d=bart.get_name()
print(d)
bart.set_name('Lack')
print(bart.get_name())