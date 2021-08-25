def main():
    name=['Dennis','Andreas','Peter']
    num=[3,1,2]
    print('输入姓名及对应编号：','\n',name,'\n',num)
    for i in range(len(name)-1):
        if name[i]>name[i+1]:
            temp=name[i]
            name[i]=name[i+1]
            name[i+1]=temp
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
    dict1=dict.fromkeys(name)
    n=0
    for i in name:
        dict1[i]=num[n]
        n+=1
    print(dict1) #(a)

    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            temp=name[i]
            name[i]=name[i+1]
            name[i+1]=temp
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
    dict1=dict.fromkeys(num)
    n=0
    for i in num:
        dict1[i]=name[n]
        n+=1
    print(dict1) #(b)

main()