data=input("x1,y1=（用逗号隔开）")
data=data.split(',')
x1,y1=[eval(x) for x in data]
r=eval(input("r="))
data=input("x2,y2=（用逗号隔开）")
data=data.split(',')
x2,y2=[eval(x) for x in data]
if (x2-x1)**2+(y2-y1)**2<=r**2:
    print("点(%f,%f)在圆内"%(x2,y2))
elif (x2-x1)**2+(y2-y1)**2>r**2:
    print("点(%f,%f)在圆外"%(x2,y2))
