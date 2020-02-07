X = [[1,3,3],
     [0,1,3],
     [0,0,1]]

Y = [[1,0,0],
     [1,1,0],
     [1,1,1]]

R = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        R[i][j] = X[i][j] + Y[i][j]

for r in R:
    print(r)
