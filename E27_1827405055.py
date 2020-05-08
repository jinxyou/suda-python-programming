n=eval(input("n="))
row=[x for x in range(1,n+1)]
col=[x for x in range(1,n+1)]
mat=[]
for i in range(n):
    mat.append([' ']*n) #建立矩阵
for i in range(n):
    for j in range(n):
        if row[i]<col[j]:
            continue #去掉上三角
        else:
            mat[i][j]=str(row[i]*col[j])

#输出
print('  ',end='  ')
for i in range(n):
    print("%2d"%row[i],end='  ')
print()
for i in range(n):
    print("%2d"%col[i],end='  ')
    for j in range(n):
        print("%2s"%mat[i][j],end='  ')
    print()
