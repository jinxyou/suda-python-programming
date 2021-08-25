def main():
    a=eval(input("请输入一个整数:"))
    print("%d的所有因子的和为:%d"%(a,sumf(a)))

def sumf(x):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    return sum

main()