def reverse(x):
    data=x.split(' ')
    data.reverse()
    res=' '
    return res.join(data)

def main():
    print("输入字符串：Hello the World!")
    print(reverse("Hello the World!"))

main()