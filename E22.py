x=input("请输入x=")
n=len(x)
print("x是%d位数"%n)
num=[eval(x[i]) for i in range(n)]
for i in range(n):
    print(num[i],end=' ')
print()
num.reverse()
for i in range(n):
    print(num[i],end='')
