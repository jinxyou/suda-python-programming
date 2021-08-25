with open(r"folder\file1.txt",'r') as f:
    data1=f.readlines()
with open(r"folder\file2.txt",'r') as f:
    data2=f.readlines()
with open(r"folder\file3.txt",'r') as f:
    data3=f.readlines()
with open(r"folder\file4.txt",'r') as f:
    data4=f.readlines()
with open(r"folder\merge.txt",'w') as f:
    for i in data1:
        f.write(i)
    f.write('\n')
    for i in data2:
        f.write(i)
    f.write('\n')
    for i in data3:
        f.write(i)
    f.write('\n')
    for i in data4:
        f.write(i)