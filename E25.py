x=input("请输入一个字母")
a=ord(x)
if 97<=a<=122:
    b=a-32
elif 65<=a<=90:
    b=a+32
else:
    b=a
print(chr(b))