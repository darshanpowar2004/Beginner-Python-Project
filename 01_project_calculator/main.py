# Python Calculator

operator = input("Enter the operator you want to use (+, -, *, /): ")
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

if operator == "+":
    print(f"The addition of {number1} and {number2} is {round(number1 + number2)}")

elif operator == "-":
    print(f"The subtraction of {number1} and {number2} is {round(number1 - number2)}")

elif operator == "*":
    print(f"The multiplication of {number1} and {number2} is {round(number1 * number2, 2)}")

elif operator == "/":
    print(f"The division of {number1} and {number2} is {round(number1 / number2, 2)}")

else:
    print(f"{operator} is an invalid operator!")
