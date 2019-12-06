L = []
for x in range(1,11):
    L.append(x * x)
print(L)
print([x*x for x in range(1,11)])#列表生成式
print([x*x for x in range(1,11) if x %2 == 0])
print([m+n for m in 'abc' for n in 'xyz'])
import os
print([d for d in os.listdir('.')])#列出当前目录下文件和目录
L1 = ['Hello', 'World', '18', 'Apple', 'None']
print([s.lower() for s in L1])
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])