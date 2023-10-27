import random

print("Heads or Tails Program")

print("The coin is flipped and it is: ")
random_number = random.randint(0,1)
if random_number == 0: # Heads
    print("Heads")
else:
    print("Tails")