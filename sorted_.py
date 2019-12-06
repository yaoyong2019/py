list1 = [36, 5, -12, 9, -21]
sort1 = sorted(list1,key = abs)
#sorted list排序
print(sort1)
str1 = ['bob', 'about', 'Zoo', 'Credit']
str2 = sorted(str1,key = str.lower,reverse=True)
#sorted list排序，Key关键字
print(str2)
from operator import itemgetter#list排序
L = [('Bob',75),('Adam',92),('Bart',68),('Lisa',89)]
L1 = sorted(L,key=itemgetter(0))
L2 = sorted(L,key=itemgetter(1),reverse=True)
L3 = sorted(L,key=lambda t:t[1])
print(L1)
print(L3)
print(L2)
