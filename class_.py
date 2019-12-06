class Student():
    def __init__(self,name,sroce):
        self.name = name
        self.sroce = sroce
    def print_sroce(self):
        print('%s:%s' % (self.name,self.sroce))
    def get_great(self):
        if self.sroce >= 90:
            return 'A'
        elif self.sroce >= 60:
            return 'B'
        else :
            return 'C'
bart = Student('Bart Simpson',59)
print(bart.name)
bart.print_sroce()
print(bart.get_great())