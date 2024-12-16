# Python credit card validator program

sum_odd_digits = 0
sum_second_digits = 0
total = 0

# Step 1
card_num = input("Enter your card number :- ")
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]

# Step 2
for i in card_num[::2]:
    sum_odd_digits += int(i)

# Step 3
for i in card_num[1::2]:
    i = int(i) * 2
    if i >= 10:
        sum_second_digits += (1 + (i % 10))
    else:
        sum_second_digits += i

# Step 4
total = sum_second_digits + sum_odd_digits

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
