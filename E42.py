def main():
    str=input()
    n=eval(input())
    data=[]
    res=''
    data=[str[i] for i in range(len(str))]
    del(data[n-1])
    str1=res.join(data)
    print(str1)

main()