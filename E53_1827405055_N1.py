def main():
    setA={1,2,3}
    setB={2,3,4}
    print("A:")
    for i in setA:
        print('%5d'%i,end='')
    print("\nB:")
    for i in setB:
        print('%5d'%i,end='') #(a)
    print()
    AorB=set.union(setA,setB)
    AandB=set.intersection(setA,setB)
    for i in range(3):
        trial1=eval(input("A|B="))
        trial2=eval(input("A&B="))
        if trial1==AorB and trial2==AandB:
            print("Correct!")
            break
        print("Wrong!")
    else:
        print(AorB,'\n',AandB)

main()