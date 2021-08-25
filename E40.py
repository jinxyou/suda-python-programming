def fibonacci(n):
    if n<=2:
        return 1
    if n>=3:
        return fibonacci(n-1)+fibonacci(n-2)

def main():
    n=int(input("请输入斐波那契数列的项数："))
    print("该项的值为%d"%fibonacci(n))

main()