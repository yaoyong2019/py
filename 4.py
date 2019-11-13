import math
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny

r = move(100,100,100,math.pi/0.1)
s = move(100,100,100,math.pi/0.2)
t1 = move(100,100,100,math.pi/0.3)
t2 = move(100,100,100,math.pi/1.1)
print (r,'\n',s)
print(t1,'\n',t2)
