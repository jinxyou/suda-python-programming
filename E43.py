def main():
    str='What a wonderful day!'
    print("输入一句话:What a wonderful day!")
    data=[]
    res=' '
    data=str.split(' ')
    data.reverse()
    str1=res.join(data)
    print(str1)

main()