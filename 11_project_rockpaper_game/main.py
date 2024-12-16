# Rock Paper Scissors

import random

choices =  ("rock","paper","scissors")
playing = True

games = 0
win = 0
draw = 0
lose = 0

while playing:

    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Enter a choice (rock,paper,scissors) or (q to quit): ").lower()

    games += 1

    print(f"Player = {player}")
    print(f"Computer = {computer}")

    if player == computer:
        print("Game is Draw !")
        draw += 1
    elif player == "rock" and computer == "scissors":
        print("You win !")
        win += 1
    elif player == "paper" and computer == "rock":
        print("You win !")
        win += 1
    elif player == "scissors" and computer == "paper":
        print("You win !")
        win += 1
    else:
        print("You lose !")
        lose += 1

    if not input("play agin (y/n) : ").lower() == "y":
        playing = False

print("------------------------------")
print("            RESULT            ")
print("------------------------------")

print(f"You Playing games = {games}")
print(f"You win = {win}")
print(f"You lose = {lose}")
print(f"You draw = {draw}")
