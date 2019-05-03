print("Enter the numbers you wanna compare")
d = int(input())
a = int(input())
if (d>0 and a>0):
    print("Both are Positive numbers")
elif (d>0 and a<0):
    print("a is a Negative number")
elif (d<0 and a>0):
    print("d is a Negative number")
else:
    print("Both are Negative numbers")




