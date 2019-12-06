print(type(123))
#基本类型都可以用type()判断：
a = type(str)
b = type(None)
c = type(abs)
print(a,b,c)

import types
def fn():
    pass

f= type(fn)
print(f)
f1 = (type(fn)==types.FunctionType)
f2 = (type(abs)==types.BuiltinFunctionType)
f3 = (type(lambda x: x)==types.LambdaType)
f4 = (type((x for x in range(10)))==types.GeneratorType)
print(f1,f2,f3,f4)

#我们要判断class的类型，可以使用isinstance()函数

import jicheng_duotai
a = jicheng_duotai.Animal()
b = jicheng_duotai.Dog()
c = jicheng_duotai.Husky()

t = isinstance(c,jicheng_duotai.Husky)
t2 = isinstance(c,jicheng_duotai.Dog)
t3 = isinstance(c,jicheng_duotai.Animal)

print(t,t2,t3)

#使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
#print(dir('abc'))
print('abc'.__len__())
class MyDog(object):
    def __len__(self):
        return 100
mdog = MyDog()
m = mdog.__len__()
n= len(mdog)
print(m,n)
print('Abc'.lower())

#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class Myobject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = Myobject()
p1 = hasattr(obj,'x')
p2 = hasattr(obj,'y')
setattr(obj,'y',19)
p3 = hasattr(obj,'y')
p4 = getattr(obj,'y')
print(p1,p2,p3,p4)
print(obj.x+obj.y)
