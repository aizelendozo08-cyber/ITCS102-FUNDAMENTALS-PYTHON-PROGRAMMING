num = eval(input ("Enter a number :"))
result = 1

for i in range (num, 0, -1):
    result *= i
    print("The factorial:", result)
