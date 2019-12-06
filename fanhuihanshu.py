def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
f= calc_sum(3,5,7,9)
print(f)
def lazy_sum(*args):
    def sum():#“闭包（Closure）”的程序结构
        ax = 0
        for n in args:
            ax+=n
        return ax
    return sum
f1 = lazy_sum(3,5,7,9)
f2 = lazy_sum(3,5,7,9)
print(f2())
print(f1==f2)#
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return f
p1 = count()
p2 = count()
p3 = count()
print(p1(),p2(),p3())
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
def createCounter():
    def c(i):
        def d():
            return i
        return d
    str1 = []
    for j in range(1,9):
        str1.append(c(j))
    return str1
w1= createCounter()
print(w1(),w1(),w1())