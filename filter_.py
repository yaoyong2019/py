def is_odd(n):
    return  n % 2 == 1
s = list(filter(is_odd,[1,2,3,4,5,6,7,6,8,4]))
print(s)

def not_empty(s):
    return s and s.strip()
s1 = list(filter(not_empty,['A','B','90','RT','er','',' ']))
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留
print(s1)
def _odd_iter():
    n = 1
    while True:
        n=n+2
        yield n
# def _not_divisible(n):
#     return lambda x:x%n>0
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n),it)
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
def is_palindrome(n):
    # print(n)
    str1 = str(n)
    # print(str1)
    str2 = str1[::-1]
    # print(str2)
    m = int(str2)
    # print(m)
    # if m == n:
    #     return True
    # else:
    #     return False
    return m == n
output = filter(is_palindrome, range(1,80))
print(list(output))


