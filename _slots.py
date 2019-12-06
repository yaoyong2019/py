# class Student(object):
#    # __slots__ = ('name','age')#用tuple定义允许绑定的属性名称
#     def get_score(self):
#         return self.score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value<0 or value>100:
#             raise ValueError('score must between 0~100')
#         self.score = value

# s = Student()
# # s.name = 'Bob'
# # s.age = 29
# s.set_score(90)
# p = s.get_score()
# print(p)

#@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('')
        if value<0 or value>100:
            raise ValueError('')
        self._score = value
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2019-self._birth


s = Student()
s.score = 60
s.birth = 2001
print(s.score)
print(s.birth,s.age)