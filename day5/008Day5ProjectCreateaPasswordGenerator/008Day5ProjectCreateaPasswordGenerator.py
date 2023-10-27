import random
import characters

print("Welcome to pyPassword Generator")

no_letters = int(input("How many letters would you like in your password? "))
no_numbers = int(input("How many numbers would you like in your password? "))
no_symbols = int(input("How many symbols would you like in your password? "))

password = ""

# choosing letters
size_letters = len(characters.letters)
for i in range (0, no_letters):
    password += random.choice(characters.letters)

# choosing symbols
size_symbols = len(characters.symbols)
for i in range (0, no_symbols):
    password += random.choice(characters.symbols)

# choosing symbols
size_numbers = len(characters.numbers)
for i in range (0, no_numbers):
    password += random.choice(characters.numbers)

print(f"Your password is: {password}")

#shuffling password
list_password = []
for i in range (0,len(password)):
    list_password.append(password[i])

random.shuffle(list_password)
shuffle_password = ""
for char in list_password:
    shuffle_password += char

print(f"Your shuffled password is: {shuffle_password}")
