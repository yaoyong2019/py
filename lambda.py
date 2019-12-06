p = list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
print(p)
f = lambda x:x*x#关键字lambda表示匿名函数，冒号前面的x表示函数参数
g = lambda x,y: x * x + y * y
print(f(5))
print(g(3,5))
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L1 = list(filter(lambda n:n%2==1,range(1,20)))
print(L1)