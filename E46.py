def main():
    import re
    x = 'This  is  very funny and   cool,indeed!'
    print(x)
    pat1 = re.compile(' +')
    x = pat1.sub(' ', x)
    pat2 = re.compile('([,.:;?!])(\w+)')
    x = pat2.sub(r'\1 \2', x)
    print(x)

main()