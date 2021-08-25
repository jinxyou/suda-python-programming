with open("Numbers.txt","r") as f:
    data=f.readlines()
newdata=[]
for i in data:
    newdata.append(eval(i))
newdata.sort()
avg=0
for i in newdata:
    avg+=i
avg/=len(newdata)
var=0
for i in newdata:
    var+=(i-avg)**2/len(newdata)
with open("Sort.txt","w") as f:
    for i in data:
        f.write(i)
    f.write('\n')
    f.write(str(avg))
    f.write('\n')
    f.write(str(var))