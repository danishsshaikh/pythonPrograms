def mul_or_sum(num1, num2):
    product = num1 * num2
    if(product < 1000):
        return product
    else:
        return num1 + num2

number1 = int(input("Enter First Number "))
number2 = int(input("Enter Second Number "))

result = mul_or_sum(number1, number2)
print("The Result is", result)
