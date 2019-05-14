n = str(input("Enter the String\n"))
lc = 0
uc = 0
for alphabet in n:
    if alphabet.isupper():
        uc = uc+1
    else:
        lc = lc+1
print("Lower Case is",uc)
print("Upper Case is",lc)
