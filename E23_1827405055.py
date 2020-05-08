data=input("请输入三个数（用空格隔开）")
data=data.split(' ')
data=[eval(x) for x in data]
data.sort()
for i in range(3):
    print(data[i],end=' ')
print()