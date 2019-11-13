names = ['Bob','Jack','Tiffly']
for name in names:
    print(name)
sum = 0
for x in range(101):
    sum = sum + x
    if x > 9:
        print (x)
        break    
print(sum)
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for LL in L:
    print('Hello,'+LL)
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

    d = {'Bob':95,'Tiffly':97,'Jack':87}
    print (d['Bob'])