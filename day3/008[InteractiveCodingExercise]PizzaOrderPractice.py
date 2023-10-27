print("Welcome to Python Pizza Deliveries!")

size= input("What size of pizza do you want? S, M, or L. ")
add_pepperoni = input("Do you want extra pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")

if size == 'S':
    pizza_price = 15
    if add_pepperoni == 'Y':
        pizza_price += 2
elif size == 'M':
    pizza_price = 20
    if add_pepperoni == 'Y':
        pizza_price += 3
elif size == 'L':
    pizza_price = 25    
    if add_pepperoni == 'Y':
        pizza_price += 3
else:
    print("You didn't choose the correct size of pizza! try again")

if extra_cheese == 'Y':
    pizza_price += 1

print(f"Ypur final bill is: ${pizza_price}")