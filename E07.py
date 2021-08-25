import math
def side(x1,y1,x2,y2):
    x=math.sqrt(((x1-x2)**2+(y1-y2)**2))
    return x

x1=eval(input("x1="))
y1=eval(input("y1="))
x2=eval(input("x2="))
y2=eval(input("y2="))
x3=eval(input("x3="))
y3=eval(input("y3="))
side1=side(x1,y1,x2,y2)
side2=side(x1,y1,x3,y3)
side3=side(x2,y2,x3,y3)
s=(side1+side2+side3)/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print("{:<7.2f}".format(area))