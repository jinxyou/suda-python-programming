i=2
n=0
aList=[]
for x in range(2,500):
    for i in range(2,500):
        if i>=x:
            aList.append(x)
            break
        if x%i==0:
            break
for j in aList:
    print(j,end=' ')
    n+=1
    if n%5==0:
        print("")