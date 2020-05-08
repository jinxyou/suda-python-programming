import math
data=input("a,b,c=（用逗号隔开)")
data=data.split(',')
a,b,c=[eval(x) for x in data]
delta=b**2-4*a*c
if a==0:
    print("无意义")
else:
    if delta>0:
        delta=math.sqrt(delta)
        x1=(-b+delta)/2*a
        x2=(-b-delta)/2*a
        print("x1=%10.5f\nx2=%10.5f"%(x1,x2))
    elif delta==0:
        print("%10.5f"%((-b)/2*a))
    elif delta<0:
        delta = math.sqrt(-delta)
        x1=complex(((-b)/2*a),(delta/2*a))
        x2=complex(((-b)/2*a),(delta/2*a))
        print(x1)
        print(x2)
