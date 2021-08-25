newname=input("Input a name:")
with open("names.txt","r") as f:
    data=f.readlines()
for i in range(len(data)):
    if newname<data[i]:
        data.insert(i,newname+'\n')
with open("names.txt","w") as f:
    for i in data:
        f.write(i)