# Compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = int(input("Enter your principal amount : "))
    if principal <= 0:
        print("principal can't be less than or equal to zero.\n")

while rate <= 0:
    rate = float(int(input("Enter your interest rate  : ")))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero\n")

while time <= 0:
    time = int(input("Enter your time in years : "))
    if time <= 0:
        print("Time in years can't be less than or equal to zero\n(")

final_amount = principal * pow(1+(rate/100),time)

print(f"Balance after {time} year/s: ₹{final_amount:.2f}")

