def main():
    dict1={'num':1,'name':'Andreas','position':'Support'}
    dict2={'num':2,'name':'Nicolai','stats':'+'}
    list1=[]
    for i in dict1.keys():
        for j in dict2.keys():
            if i==j:
                list1.append(i)
    print(list1)

main()