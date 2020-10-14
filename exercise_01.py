def sum(a,b):
    sum = a + b
    return sum
ans = sum(2,2) 
print("Result of sum:\n", ans, "\n")

import numpy as np

def matmult(mat1, mat2):
    res=np.zeros((3,3))
    for i in range (len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j]+=mat1[i][k] * mat2[k][j]
    
    return res

X=np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
Y=np.array([[4, 5, 6], [4, 5, 6], [4, 5, 6]])

res_self=matmult(X,Y)
res_np=np.matmul(X,Y)

print("Result of own function:\n", res_self, "\n")

print("Result of np.matmul:\n", res_np, "\n")
