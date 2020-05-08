n=eval(input("Please input the number of rows:"))
m=eval(input("Please input the number of columns："))
A,B,C=[],[],[]
for i in range(n):
    A.append([0]*m)
    B.append([0]*m)
    C.append([0]*m)
for i in range(n):
    for j in range(m):
        A[i][j]=eval(input("Please input A[%d,%d]: "%(i,j)))
for i in range(n):
    for j in range(m):
        B[i][j]=eval(input("Please input B[%d,%d]: "%(i,j)))
        C[i][j]=A[i][j]+B[i][j]
print(C)