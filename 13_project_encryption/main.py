# Python Encryption

import random
import string

chars = " "+string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

# Encryption

massage = input("Enter Your Massage: ")
encrypted_massage = ""

for letter in massage:
    index = chars.index(letter)
    encrypted_massage += keys[index]

print(f"original massage : {massage}")
print(f"Encrypted massage : {encrypted_massage}")


# Decrypt

encrypted_massage = input("Enter Your Massage: ")
massage = ""

for letter in encrypted_massage:
    index = keys.index(letter)
    massage += chars[index]

print(f"original massage : {encrypted_massage}")
print(f"Encrypted massage : {massage}")
