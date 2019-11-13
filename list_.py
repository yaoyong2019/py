a = [10,20,30,40]
a2 = list(range(8))
a3 = list(range(10,80,5))
print(a2)
a.append(49)#添加元素
a.extend(a2)#添加列表
a.insert(0,0.1)#按索引插入元素
a.insert(0,0.1)
a.insert(0,0.1)
a.remove(0.1)#删除元素
a.pop(-2)#按索引删除元素
print(a.index(20),' ',end='')#元素索引位置
print(a.count(0.1))#元素个数统计
print(a.count(0.01))    #判断元素是否存在
print(len(a))#元素长度
a2.clear()#删除所有元素
print(a2)
a.reverse()#元素倒置
a2 = [10,20,30,40,1,3,23]
a2.reverse()
for i in a2:
    print(i,' ',end="")
print()
a2.sort()
for i in a2:
    print(i,' ',end="")
print()
for i in a3:
    print(i,' ',end="")
a4 = a
print()
print(a4)
print(a)
a.reverse()
print(a)
print(a4)
a4 = a.copy()#复制列表
a.reverse()
print(a)
print(a4)
a.sort(reverse=1)#倒序排列
print(a)
def tkey(e):
    return e[1]
random = [(3,2),(2,5),(5,3),(4,1),(3,3)]
random.sort(key = tkey)#按第二个元素排序
print(random)
a5 = a2 + a3
a2 = range(8)

print(a5[1:6])
print(max(a5))