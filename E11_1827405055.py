import random
import math
a=random.uniform(10,50)
b=random.uniform(10,50)
c=complex(a,b)
m=math.sqrt(a**2+b**2)
angle=math.atan(b/a)
print("复数为{:>7.2f}".format(c))
print("复数的模为{:>7.2f}".format(m))
print("辐角为{:>7.2f}".format(angle))