dict = {'Bob':95,'Jack':90,'Mark':89,'Jine':87}
print(dict)
dict['Paul'] = 97
dict['Rick'] = 83
print(dict['Jack'])

dict['Paul'] = 90
# del dict['Jine']#删除元素
# dict.clear()#清空元素
# del dict#删除字典
# print(len(dict))
# print(str(dict))
# print(type(dict))
# pop_ = dict.pop('Bob')#删除并返回值
# print(pop_)

# set1 = {'paul','mary','lili','4','a','2'}
# print(set1)
set2 = {'a','2','r'}
# set3 = set1 ^ set2# - | & ^
# print(set3)
set2.add('ppp')#添加元素
set2.update('ppp','vv','of')#添加元素
print(set2)
set2.remove('a')#删除元素
set2.discard('ppp')#删除元素不返回错误
set2.pop()#随机删除元素
print(set2)
#set2.clear()#清空集合

print(set4)