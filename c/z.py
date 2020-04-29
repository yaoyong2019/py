from enum import Enum
Month = Enum('month',('jan','Feb','Mar','Apr','may','Jun','Sep','Oct','Nov','Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)