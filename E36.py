import math
def isMersenne(x):
    for p in range(x):
        if 2**p-1==x and isPrime(x) is True:
            return p
            break
    else:
        return -1

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
            break
    else:
        return True

def main():
    print("{:>3s}".format("p"), end=' ')
    print("{:>4s}".format("2**p-1"), end='')
    print()
    for i in range(1000):
        p=isMersenne(i)
        if p!=-1:
            print("{:>3d}".format(p),end='')
            print("{:>4d}".format(i),end='')
            print()

main()