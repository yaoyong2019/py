d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():#分别迭代KEY，VALUE
    print(k,v)
for i,value in enumerate(['a','b','c']):#同时迭代索引和元素本身
    print(i,value)
for x,y in [(1,2),(3,4),(8,9)]:#
    print(x,y)
a = [2,78,45,0,5,785,-20,45,22,-2,443]
def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for i,value in enumerate(a):
        if max > L[i]:
            max = L[i]
        if min < L[i]:
            min = L[i]
    return(max,min)
print(findMinAndMax(a))