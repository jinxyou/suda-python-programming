def main():
    import random
    set1=set()
    set2=set()
    for i in range(201):
        set1.add(random.randint(0,500))
        set2.add(random.randint(0,500))
    set3=set1.symmetric_difference(set2)
    n=0
    print("不相同的数据：")
    for i in set3:
        print("%5d"%i,end='')
        n+=1
        if n==10:
            print()
            n=0
    set4=set.intersection(set1,set2)
    print()
    n=0
    print("相同的数据：")
    for i in set4:
        print("%5d"%i,end='')
        n+=1
        if n==10:
            print()
            n=0

main()