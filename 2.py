tg = float(input('tizhong:'))
sg = float(input('shengao:'))
bmi = tg / (sg*sg)
print('你的身高是'+str(sg*100)+'cm，你的体重是'+str(tg)+'kg，你的BMI指数是：'+'%.2f' % bmi)
if bmi > 32 :
    print('ni de tizhong +++!','%.2f' % bmi)
elif bmi > 28 :
    print('ni de tizhong ++!','%.2f' % bmi)
elif bmi > 25 :
    print('ni de tizhong +!','%.2f' % bmi)
elif bmi > 18.5 :
    print('ni de tizhong Yes!','%.2f' % bmi)
else :
    print('ni de tizhong -!','%.2f' % bmi)
    
#ceshi tongbu!
#ceshi2 zaitongbu
