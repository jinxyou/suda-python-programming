def main():
    tag='<composer>Wolfgang Amadeus Mozart</composer>\n<author>Samuel Beckett</author>\n<city>London</city>'
    print(tag)
    print()
    import re
    res=re.sub('</[a-zA-Z]+>','',tag)
    res=re.sub('<','',res)
    res=re.sub('>',':',res)
    print(res)

main()