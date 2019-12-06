names = ['adam', 'LISA', 'barT']
def normlize(name):    
    return name.title()
l1 = list(map(normlize,names))#所有单词首字母大写，map
print(l1)

from functools import reduce
def fn(m,n):
    return m * n
# s = reduce(fn,[2,3,4,5,6])#list列表乘积
# print(s)
def prod(L):
    return reduce(fn,L)
s = prod([3,5,7,9])
print(s)

dn = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}
def str2int(s):
    ints = map(lambda ch : dn[ch], s)
    return reduce(lambda x,y:x*10+y, ints)
print(str2int('0123'))

def str2float(s):
    nums = map(lambda ch:dn[ch],s)
    point = 0
    def to_float(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float,nums)
print(str2float('0'))
print(str2float('123.236'))
