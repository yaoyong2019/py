g = (x * x for x in range(10))
print(g)
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'
print(fib(10))
f = fib(6)
print(f)
def triangles(n):
    I,index = [1],0
    while index < n:
        yield I
        I = [1] + [I[i] + I[i+1] for i in range(len(I)-1)] + [1]
        index += 1
for i in triangles(4):
    print(i)

