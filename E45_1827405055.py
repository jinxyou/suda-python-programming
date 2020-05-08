def main():
    import re
    s=input()
    if s.endswith('y'):
        s=re.sub('y$','ies',s)
    elif re.findall('[osxz(sh)(ch)]$',s):
        s+='es'
    else:
        s+='s'
    print(s)

main()