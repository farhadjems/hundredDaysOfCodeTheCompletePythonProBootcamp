print("Welcome to the Love Calculator!")

name1 = input("What is your name?\n ").lower()
name2 = input("What is their name?\n ").lower()

true_digit = 0
love_digit = 0

#true
true_digit += name1.count("t") + name2.count("t")
true_digit += name1.count("r") + name2.count("r")
true_digit += name1.count("u") + name2.count("u")
true_digit += name1.count("e") + name2.count("e")

love_digit += name1.count("l") + name2.count("l")
love_digit += name1.count("o") + name2.count("o")
love_digit += name1.count("v") + name2.count("v")
love_digit += name1.count("e") + name2.count("e")

score = str(true_digit) + str(love_digit)
score = int (score)

print(f"Your score is {score}")

if score < 10 or score > 90: 
    print("You go together like coke and mentos.")
elif score > 40 and score < 50:
    print("You are alright together.")
else:
    print("")