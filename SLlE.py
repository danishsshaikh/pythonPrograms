a = []
n = int(input("Enter Number of Elements:"))

for i in range(1,n+1):
    b = input("Enter Element:")
    a.append(b)
print("The List is",a)

a.sort(key = len)
print("The List after Sorting is:",a)
