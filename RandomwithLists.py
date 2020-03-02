import random

a = []

n = int(input("Enter Number of Elements"))

for j in range(n):
    a.append(random.randint(1,20))

print("Random Generated List is:",a)
