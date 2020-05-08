n=eval(input("n = "))
i=2
aList=[]
for x in range(2,n):
    for i in range(2,n):
        if i>=x:
            aList.append(x)
            break
        if x%i==0:
            break
for i in range(len(aList)-1):
    print(aList[i],end=", ")
print(aList[len(aList)-1])