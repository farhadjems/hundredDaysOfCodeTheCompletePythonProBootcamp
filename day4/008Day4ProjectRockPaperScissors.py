import random

art_RPS = [
    #Rock
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
# Paper
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", 

# Scissors
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]



RPS = ["Rock", "Paper", "Scissors"]

user_choice = int(input(f"What do you choose? 0 {RPS[0]}, 1 {RPS[1]}, 2 {RPS[2]}\n"))

system_choice = random.randint(0,2)

if user_choice >=3 or user_choice <0:
    print("you entered an invalid number, You lose!")
else:
    print(f"You choose: {art_RPS[user_choice]}\n")
    print(f"Computer chooses: {art_RPS[system_choice]}\n")
    if system_choice - user_choice == 1:
        print("You Lose!")
    elif user_choice - system_choice == 1:
        print("You Win!")
    elif system_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif system_choice == 2 and user_choice == 0:
        print("You Win!")
    elif user_choice == system_choice:
        print ("Tie!")
    else:
        print("Error in determining the winner :(")


