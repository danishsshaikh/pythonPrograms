print("____Addition of matrcies____")
a = [[67,68,69],
     [69,68,67],
     [12,15,65]];
b = [[27,46,69],
     [65,88,37],
     [12,15,66]];
radd = [[0,0,0],
     [0,0,0],
     [0,0,0]];
rsub = [[0,0,0],
     [0,0,0],
     [0,0,0]];
for i in range(len(a)):
    for j in range(len(a[0])):
        radd[i][j] = a[i][j] + b[i][j];
for r in radd:
    print(r);
print("____Subtraction of matrices____")
for i in range(len(a)):
    for j in range(len(a[0])):
        rsub[i][j] = a[i][j] - b[i][j];
for r in rsub:
    print(r);
