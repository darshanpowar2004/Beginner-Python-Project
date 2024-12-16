# Python Banking Program
import time

# For Slowdown
def sleep():
    time.sleep(3)

def show_balance():
    print(f"Your Current Balance is ₹{balance:.2f}")

def deposit():
    amount = float(input("Enter your amount for deposit: ₹"))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter your amount for withdraw: ₹"))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return 0
    elif amount > balance:
        print("insufficient balance.")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Balance Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
        sleep()

    elif choice == "2":
        balance += deposit()
        sleep()

    elif choice == "3":
        balance -= withdraw()
        sleep()

    elif choice == "4":
        is_running = False
        sleep()

    else:
        print(f"{choice} that is not a valid choice")


print("Thank you! Have a nice day!")