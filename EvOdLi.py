a = []
n = int(input("Enter Number Of Elements:"))
for i in range(1, n+1):
    b = int(input("Enter Element:"))
    a.append(b)
print("The Elements in the List are:", a)
even = []
odd = []
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The Even List is:", even)
print("The Odd List is:", odd)
