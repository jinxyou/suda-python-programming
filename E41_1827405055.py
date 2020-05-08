def main():
    s='python'
    print(s)
    data=[]
    res=''
    s1=''
    if len(s)>=2:
        data.append(s[0])
        data.append(s[1])
        data.append(s[-2])
        data.append(s[-1])
        s1=res.join(data)
    print(s1)

main()