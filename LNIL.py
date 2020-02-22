a=[]
n=int(input("Enter number of elements:"))
print("Your given Array is:",a)

for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
    print("Insertion in Array:",a)
a.sort()

print("The Sorted Array is:",a)
print("Largest element is:",a[n-1])
