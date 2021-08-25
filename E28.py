n=eval(input("n="))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=' ')
    for j in range(n+i):
        print("*",end=' ')
        print(" ",end=' ')
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(n*2-2,i,-1):
        print("*",end=' ')
        print(" ",end=' ')
    print()