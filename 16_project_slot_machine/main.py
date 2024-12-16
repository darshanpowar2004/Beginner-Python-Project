# Slot Machine program

import random

def spin_row():
    symbols = ["🍒" ,"🍉" ,"🍋" ,"🔔" ,"⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**********************")
    print(" | ".join(row),)
    print("**********************")


def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0]=='🍒':
            return bet * 2

        elif row[0]=='🍉':
            return bet * 3

        elif row[0]=='🍋':
            return bet * 4

        elif row[0]=='🔔':
            return bet * 5

        elif row[0]=='⭐':
            return  bet * 6

    else:
        return 0


def main():
    print("***************************")
    print("Welcome to python slot game")
    print("***************************")
    print()
    print("Symbols : 🍒 🍉 🍋 🔔 ⭐")
    print()
    print("***************************")

    balance = 100
    while balance > 0:

        print(f"Your current balance is ${balance}.")

        bet = input("Enter your bite amount : $")

        if not bet.isdigit():
            print("please enter valid Number.")
            continue

        bet = int(bet)

        if  bet <= 0:
            print("bet must be greater than 0")
            continue

        if bet > balance:
            print("Insufficient funds")
            continue

        balance -= bet

        row = spin_row()
        print("spinning...")

        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"you win this round and you win ${payout}")

        else:
            print("you loss this round")

        payout += balance

        choice = input("You want to play agin (Y/N) : ").upper()

        if choice != "Y":
            break

    print("*********************")
    print(f"Balance : ${balance}")
    print("*********************")

    print("GAME OVER")


if __name__=='__main__':
    main()