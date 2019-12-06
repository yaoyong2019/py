#__str__
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__
print(Student('Bob'))
s= Student('Jack')
print(s)

#__iter__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self#实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, (self.a + self.b)
        if self.a > 100:
            raise StopIteration()
        return self.a
        
# for i in Fib():
#     print(i)

class Fib2(object):
    def __getitem__(self,n):
        a, b = 1, 1
        for x in range(n):
            a,b = b,a+b
        return a

f = Fib2()
print(f[2])#qiepian shibai

class Fib3(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1, 1
            L = []
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a, b = b ,a+b
            return L

f3 = Fib3()
print(f3[3])
print(f3[:5])
                    