import numpy as np
n=9
m=3
i=0
j=0
arr=[]
print("start entering 9 elements now")
arr=[int(input()) for i in range(n)]
k1=[arr[0],arr[1],arr[2]]
k2=[arr[3],arr[4],arr[5]]
k3=[arr[6],arr[7],arr[8]]

for i in range(m):
    avg1=np.mean(k1)
    avg2=np.mean(k2)
    avg3=np.mean(k3)
    
    print ("k1 :- ",k1,avg1)
    print ("k2 :- ",k2,avg2)
    print ("k3 :- ",k3,avg3)
    print (" ")
   
    k1.clear()
    k2.clear()
    k3.clear()
    for j in range(n):
        if(min(abs(avg1-arr[j]),abs(avg2-arr[j]),abs(avg3-arr[j]))==abs(avg1-arr[j])):
            k1.append(arr[j])
                   
        elif(min(abs(avg1-arr[j]),abs(avg2-arr[j]),abs(avg3-arr[j]))==abs(avg2-arr[j])):
            k2.append(arr[j])
                    
        elif(min(abs(avg1-arr[j]),abs(avg2-arr[j]),abs(avg3-arr[j]))==abs(avg3-arr[j])):
            k3.append(arr[j])
             

print("final clustering output:- ")
print("k1: ",k1)
print("k2: ",k2)
print("k3: ",k3)

