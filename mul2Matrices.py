X = [[1,2],
     [4,5],
     [7,8]]

Y = [[1,2],
     [4,5],
     [7,8]]

R = [[0,0],
     [0,0],
     [0,0]]


for i in range(len(X)):
    for j in range(len(X[0])):
        R[i][j] = X[i][j]*Y[i][j]

for r in R:
    print(r)
