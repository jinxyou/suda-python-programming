a=eval(input("a="))
n=eval(input("n="))
num=[]
S=0
for i in range(n):
    num.append(0)
    num[i]=(10**(i+1)-1)//9*a
    S+=num[i]
print(S)