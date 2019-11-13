def person(name,age,**kw):#关键字参数dict
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack',24,**extra))
print(person('Jack',24,city='Beijing',addr='caoyang',zipcode='12345678'))
def person2(name,age,*,city,job):#命名关键字参数
    print(name,age,city,job)
# def person2(name, age, *, city, job):
#     print(name, age, city, job)
print(person2('BOB',24,city='BEijing',job='Engineer'))

def product(*y):
    s=1
    for i in y:
        s=s*i
    return s
print(product(2,3,5,5))