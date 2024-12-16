#Python Calculator

operators = input("Enter you want operators ( + , - , * , / ) : ")
number1 = float(input("Enter your first number : "))
number2 = float(input("Enter your second number : "))

if operators == "+":
    print(f"The Addition of {number1} and {number2} is \n{round(number1 + number2)}")

elif operators == "-":
    print(f"The Subtraction of {number1} and {number2} is \n{round(number1 - number2)}")

elif operators == "*":
    print(f"The Multiplication of {number1} and {number2} is \n{round(number1 * number2, 2)}")

elif operators == "/": 
    print(f"The Division of {number1} and {number2} is \n{round(number1 / number2, 2)}")

else:
    print("{operators} is Operator is invalid ! ")