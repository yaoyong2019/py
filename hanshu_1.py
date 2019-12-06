f = abs
print(f(-30))
print(f)
def add(x,y,f):#高阶函数
    return f(x) + f(y)
print(add(-3,5,abs))
def ff(x):
    return x*x
r = map(ff,[1,2,3,4,5,6,7,8,9])
print(list(r))
from functools import reduce
def add(x,y):
    return x*10+y
print(reduce(add,(1,3,4,5)))