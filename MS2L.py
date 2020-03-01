a = []
c = []

print("First List")

n1 = int(input("Enter number of elements:"))
for i in range(1, n1+1):
    b = int(input("Enter Elements:"))
    a.append(b)

print("Second List")

n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)

d = a + c
d.sort()
print("The Sorted List is:", d)
