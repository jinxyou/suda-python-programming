str1=input("请输入第一个字符串:")
str2=input("请输入第二个字符串:")
aList=list(str1)
bList=list(str2)
if sorted(aList)==sorted(bList):
    print("同构")
else:
    print("不同构")