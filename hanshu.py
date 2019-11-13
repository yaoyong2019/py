print(abs(-100.2356),max(1.2,2,56.3,-9),min(1,4,6),int('1232'),float('12.358'),bool(1),str(100))
def power(x,n=2):#默认参数
    s = 1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(8,6))
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print(add_end([1,2,3]))
print(add_end([2,3,4]))
print(add_end())
print(add_end())

def clac(*number):#可变参数list，tuple
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum
print(clac(1,2,3,4,5,6,7))

import math
def quad(a,b,c):
    if (b**2-4*a*c) < 0:
        print('False')
        return(0)
    x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2
print(quad(1,4,3))
print(quad(1,3,9))