print("Multiplication Table Maker")

number = eval(input("Enter a number:"))
print(f"\nMultiplication Table of", number)

for aizel in range(1,11):
    result = number*aizel

    print(f"{number} x {aizel} = {result}")
