lowerNum = int(input('Enter the Lower Number: '))
upperNum = int(input('Enter the Upper Number: '))


print("Prime Numbers between", lowerNum, "and", upperNum, "are: ")

for num in range(lowerNum, upperNum + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
