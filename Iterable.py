from collections.abc import Iterable
#可以直接作用于for循环的对象统称为可迭代对象：Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('123',Iterable))
print(isinstance(123,Iterable))
print(isinstance((1,2,3),Iterable))
from collections.abc import Iterator
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance((1,2),Iterator))
