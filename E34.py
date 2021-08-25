def main():
    a=int(input("请输入一个整数:"))
    print(reverse(a))

def reverse(x):
    res = ''
    str1 = str(x)
    data = [str1[i] for i in range(len(str1) - 1, -1, -1)]
    return int(res.join(data))

main()