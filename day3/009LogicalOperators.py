print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12: 
        bill = 5
        print("You pay $5.")
    elif age <= 18:
        bill = 7 
        print("You pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is gonna be OK! Have a free ride on us!")
    else:
        bill = 12
        print("You pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your finall bill is: {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


 