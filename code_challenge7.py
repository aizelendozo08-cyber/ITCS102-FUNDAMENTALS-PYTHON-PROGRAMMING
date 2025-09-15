print("ODD NUMBER SUMMATION")
print("Maglagay ng sampung numero")

odd_sum = 0
for opote in range(10):
    number = eval(input("Enter a number:"))

    if number % 2 != 0: 
        odd_sum += number

print("The sum of all odd number is", odd_sum)