def stats(x,n=0):
    if 65<=ord(x[n])<=90:
        target=[x[n],chr(ord(x[n])+56)]
    elif 97<=ord(x[n])<=122:
        target=[x[n],chr(ord(x[n])-56)]
    count=0
    for i in range(len(x)):
        if target.count(x[i])==1:
            count+=1
    return count

def main():
    x="Hello the World!"
    n=2
    print("请输入英文语句：%s"%x)
    print("请输入字符位置：%d"%n)
    print("统计位置%d的字符是%s,则在语句中出现的次数为:%d"%(n,x[n],stats(x,n)))

main()