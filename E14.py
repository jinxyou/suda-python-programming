aList=[35,46,57,13,24,35,99,68,13,79,88,46]
aList=sorted(aList)
for i in range(len(aList)-1,-1,-1):
    if aList[i]==aList[i-1]:
        del aList[i]
print(aList)