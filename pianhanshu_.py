def int2(x,base = 2):
    return int(x,base)
print(int2('10001'))
import functools
int2 = functools.partial(int,base=2)#偏函数
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
print(int2('10101'))
max2 = functools.partial(max, 10)
print(max2(3,9,108))
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。