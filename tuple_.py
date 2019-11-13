tuple1 = (1,2,3,4,5)
print(tuple1)
tuple2 = (1,)
print(tuple2)
tuple3 = (1,4,[3,5],['a','b','c'])
print(tuple3)
print(tuple3[3][0])#元素引用
tuple3[3][0] = 'f'#改变元素的值
print(tuple3[3][0])
l1 = list(tuple1)#改变类型为list
print(l1)
print(tuple1)
print(len(tuple3))
print(tuple2[2:])
print(l1[25:])
tuple4 = tuple1 + tuple2#2个元组相加
print(tuple4)
del(tuple4)#删除元组

del(l1)
