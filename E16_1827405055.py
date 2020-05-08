import random
matrix=[]
matrixl=[]
for i in range(4):
    for j in range(4):
        matrixl.append(random.randint(0,100))
    matrix.append(matrixl)
    matrixl=[]
print([[line[i] for line in matrix] for i in range(4)])
