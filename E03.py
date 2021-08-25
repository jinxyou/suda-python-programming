import math
pi=math.pi
r=eval(input("r="))
h=eval(input("h="))
V=r**2*pi*h
print("需要的桶数为",int(20000//V+1))