L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[-1:])
p = list(range(100))
print(p[:10])
print(p[10:20])
print(p[-10:])
print(p[:10:2])
print(p[::5])
t=tuple(p)
print(t[:10])
print('abcdefg'[0:3:2])#切片
def trim(s):
    print(len(s))
    n=len(s)
    while n > 0:
        if s[-n] == ' ':
            s.pop(-n)
        else:
            break
        n = n-1
    m = len(s)
    while m>0:
        if s[m-1] == ' ':
            s.pop(m-1)
        else:
            break
        m = m-1
    return s
ss = list('      i am a book.     ')
print(trim(ss))
