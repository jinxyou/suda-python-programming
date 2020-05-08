def main():
    tup=(65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)
    sum=0
    for i in tup:
        sum+=i
    avg=sum/8
    variance=0
    for i in tup:
        variance+=(i-avg)**2
    variance/=8
    print(variance)

main()