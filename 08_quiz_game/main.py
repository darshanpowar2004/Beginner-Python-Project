# Python Quiz Game.
from errno import ELOOP

questions = ("1. What is the capital of France?",
             "2. Who wrote the play 'Romeo and Juliet'?",
             "3. What is the largest planet in our solar system?",
             "4. Which element has the chemical symbol 'O'?",
             "5. What is the name of the largest ocean on Earth?")

options = (("A) Rome","B) Berlin","C) Madrid","D) Paris"),
           ("A) William Shakespeare","B) Mark Twain","C) Charles Dickens","D) Jane Austen"),
           ("A) Mars","B) Jupiter","C) Saturn","D) Venus"),
           ("A) Oxygen","B) Gold","C) Silver","D) Iron"),
           ("A) Atlantic Ocean","B) Indian Ocean","C) Arctic Ocean","D) Pacific Ocean"))

answers = ("D","A","B","A","D")
guesses = []
score = 0
questions_no = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[questions_no]:
        print(option)

    guess = input("Enter your answer (A,B,C,D) : ").upper()
    guesses.append(guess)

    if guess == answers[questions_no]:
        print("CORRECT !")
        score += 1
    else:
        print("INCORRECT !")

    questions_no += 1

print("-----------------------------")
print("           RESULT            ")
print("-----------------------------")

print("Guesses : ",end="")
for guess in guesses:
    print(guess,end=" ")

print()
print("Answers : ",end="")
for answer in answers:
    print(answer,end=" ")

print()


print("-----------------------------")
print(f"score : {int((score/len(answers))*100)}%")
print("-----------------------------")

