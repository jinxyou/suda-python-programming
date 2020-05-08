aList=[["张飞",78,75],["李大刀",92,67],["李墨白",84,88],["王老虎",50,50],["雷小米",99,98]]
tempList=["","","","",""]
for i in range(5):
    tempList[i]=aList[i][0]
    aList[i][0]=aList[i][1]+aList[i][2]
    aList[i][1]=tempList[i]
aList.sort(reverse=True)
for i in range(5):
    tempList[i]=aList[i][0]
    aList[i][0]=aList[i][1]
    aList[i][1]=tempList[i]
    del aList[i][2]
for i in range(5):
    for j in range(2):
        print(aList[i][j],end=" ")
    print()
