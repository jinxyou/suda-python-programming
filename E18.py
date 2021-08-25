n=int(input("n="))
row=0
column=(n-1)//2
mat=[]
for i in range(n):
    mat.append([0]*n)
mat[row][column]=1
for i in range(2,n**2+1):
    if mat[(row-1+n)%n][(column+1)%n ]==0:
        row=(row-1+n)%n
        column=(column+1)%n
    else:
        row=(row+1)%n
    mat[row][column]=i

for i in range(n):
    for j in range(n):
        print(mat[i][j],end=' ')
    print('')