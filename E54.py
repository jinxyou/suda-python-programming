with open("copy.txt",'r') as f:
    s=f.read();
with open("new.txt",'w') as f:
    f.write(s);