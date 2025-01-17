import string
import random
letters_list = list(string.ascii_letters)
numbers_list = list(str(i) for i in range(0,10))
characters_list = list("!#$%&/()=")

print("Welcome to password generator")

letters_qty = int(input("How many letters in your password"))
symbols_qty = int(input("How many symbols in your password"))
numbers_qty = int(input("How many symbols in your password"))

password = ''
for letter in range(0, letters_qty):
    password += random.choice(letters_list)

for numbers in range(0, numbers_qty):
    password += random.choice(numbers_list)

for symbols in range(0, symbols_qty):
    password += random.choice(characters_list)

password_list = list(password)
random.shuffle(list(password_list))
print(''.join(password_list))