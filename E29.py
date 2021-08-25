n=1
while n!=0:
    n=eval(input("Please input the number of numbers:"))
    if isinstance(n,int) is False:
        print("输入非法!")
        n=eval(input("Please input the number of numbers:"))
    if n==0:
        exit()
    num=[]
    sum=0
    for i in range(n):
        num.append(0)
        num[i]=eval(input("Please input number %d:"%(i+1)))
        if isinstance(num[i],int) is False:
            print("输入非法!")
            num[i]=eval(input("Please input number %d:"%(i+1)))
        sum+=num[i]
    print("sum =",sum)