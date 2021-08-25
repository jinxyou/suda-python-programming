def main():
    dict1={'num':1,'name':'Michal','stats':'-'}
    dict2={'num':'1','name':'Michal','stats':'+'}
    list1=[]
    for i in dict1.keys():
        for j in dict2.keys():
            if dict1[i]==dict2[j]:
                list1.append(i)
    print(list1)

main()