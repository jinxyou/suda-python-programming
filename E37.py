def encrypt(x,n=5):
    str1=''
    res=''
    x=[x[i] for i in range(len(x))]
    for i in range(len(x)):
        if 48<=ord(x[i])<=57: #按次序检验每个字符是否为数字
            str1+=x[i]
            if i!=len(x)-1: #检验当前是否为最后一个字符，防止报错
                if 48<=ord(x[i+1])<=57: #检验下一个字符是否为数字
                    continue
                else:
                    str1=str(int(str1)*n)
                    res+=str1
                    str1=''
            else:
                str1 = str(int(str1)*n)
                res+=str1
                str1 = ''
        if 65<=ord(x[i])<=85 or 97<=ord(x[i])<=117:
            res+=chr(ord(x[i])+n)
        elif 86<=ord(x[i])<=90 or 118<=ord(x[i])<=122:
            res+=chr(ord(x[i])+n-26)
    return res

def decode(x,n=5):
    str1 = ''
    res = ''
    x = [x[i] for i in range(len(x))]
    for i in range(len(x)):
        if 48 <= ord(x[i]) <= 57:
            str1 += x[i]
            if i != len(x) - 1:
                if 48 <= ord(x[i + 1]) <= 57:
                    continue
                else:
                    str1 = str(int(str1) // n)
                    res += str1
                    str1 = ''
            else:
                str1 = str(int(str1) // n)
                res += str1
                str1 = ''
        if 70 <= ord(x[i]) <= 85 or 102 <= ord(x[i]) <= 122:
            res += chr(ord(x[i]) - n)
        elif 65 <= ord(x[i]) <= 69 or 97 <= ord(x[i]) <= 101:
            res += chr(ord(x[i]) - n + 26)
    return res

x="undv12312foasdf123e"
a=encrypt(x,)
print("输入字符串：\n%s"%x)
print(a)
print(decode(a,))