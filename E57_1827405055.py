import re
with open("word.txt","r") as f:
    data=f.readlines()
for i in data[::]:
    if not re.findall('^[aouei]',i):
        data.remove(i)
with open("new_word.txt","w") as f:
    for i in data:
        f.write(i)