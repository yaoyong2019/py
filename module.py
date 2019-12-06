#module
__author__ = 'mike'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
    test()
print(__author__)
print(__name__)
def _private1(name):
    #private函数和变量“不应该”被直接引用，而不是“不能”被直接引用
    return 'Hello ,%s' % name
def _private2(name):
    return 'Hello ,%s' % name
def greeting(name):
    if len(name) > 3:
        return _private1(name)
    else:
        return _private2(name)
