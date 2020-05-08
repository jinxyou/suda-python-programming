import math

def side(x1,y1,x2,y2):
    x=math.sqrt(((x1-x2)**2+(y1-y2)**2))
    return x

crd=input("x1,y1,x2,y2,x3,y3=(用逗号隔开)")
crd=crd.split(',')
crd=[eval(x) for x in crd]
x1,y1,x2,y2,x3,y3=crd
side1=side(x1,y1,x2,y2)
side2=side(x1,y1,x3,y3)
side3=side(x2,y2,x3,y3)
s=(side1+side2+side3)/2
S=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
C=2*s

if S==0: print("无法构成三角形")
else: print("面积为%f，周长为%f"%(S,C))
