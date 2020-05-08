def delete(aList):
    aList.sort()
    for i in range(len(aList) - 1, -1, -1):
        if aList[i] == aList[i - 1]:
            del aList[i]
    return aList

def main():
    s='google.com'
    print('输入字符串：google.com\n统计所有字符出现的次数:')
    data=delete([s[i] for i in range(len(s))])
    res=[]
    for i in data:
        res.append(s.count(i))
    dict1=dict(zip(data,res))
    for keys,values in dict1.items():
        print("'%s':%d"%(keys,values),end=',')

main()