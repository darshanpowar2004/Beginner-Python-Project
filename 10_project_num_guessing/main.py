import random

lower_num = 1
higher_num = 100
num = random.randint(lower_num, higher_num)

guess = 0

print("Python Number Guessing Game.")
print(f"Select A Number Between {lower_num} to {higher_num}")
while True:
    try:
        your_num = int(input("Enter your number (1 to 100): "))


        guess += 1

        if your_num < num:
            print("The number is higher than your guess.")

        elif your_num > num:
            print("The number is lower than your guess.")

        else:
            print("----------------------------------------------")
            print(f"Your guess is correct! The number is {num}.")
            break
    except Exception as e:
        print("Invalid Guess")

print(f"You guessed the number in {guess} attempts.")
print("----------------------------------------------")
