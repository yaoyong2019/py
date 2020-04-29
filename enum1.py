from enum import Enum,unique
Month = Enum('month',('jan','Feb','Mar','Apr','may','Jun','Sep','Oct','Nov','Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = WeekDay.Mon
day2 = WeekDay['Tue']
day3 = WeekDay.Tue.value
print(day1,day2,day3)
