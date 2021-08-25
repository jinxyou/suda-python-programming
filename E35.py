import math
def reverse(x):
    res = ''
    str1 = str(x)
    data = [str1[i] for i in range(len(str1) - 1, -1, -1)]
    return int(res.join(data))

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
            break
    else:
        return True

def isantiprime(x):
    if reverse(x)!=x and isPrime(x) is True and isPrime(reverse(x)) is True:
        return True
    else:
        return False

def main():
    resList=[]
    count=0
    n=0
    i=0
    while i>=0:
        if isantiprime(i) is True:
            resList.append(i)
            #输出
            n+=1
            count+=1
            print("{:>5d}".format(i),end='')
            if n==8:
                n=0
                print()
        if count>=30:
            break
        i+=1

main()