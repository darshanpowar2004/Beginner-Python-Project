# Hangman in python.
from wordlist import words
from hangman_art import  hangman_art
import random


def display_man(wrong_guess):
    print("*****************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("*****************")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(answer)

def main():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    wrong_guess = 0
    is_running = True
    guess_words = set()

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Enter a word : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guess_words:
            print(f"{guess} is already in word.")
            continue

        guess_words.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guess += 1

        if "_" not in hint:
            display_answer(answer)
            display_answer(answer)
            print("You Win!!!")
            is_running = False

        if wrong_guess >= len(hangman_art) - 1:
            display_man(wrong_guess)
            display_answer(answer)
            print("You Lose!!!")
            is_running = False


if __name__ == "__main__":
    main()