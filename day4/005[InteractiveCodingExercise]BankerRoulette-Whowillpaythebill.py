import random

names = input("Enter names separated by comma ',': ")

list_names = names.split(', ')
# print(list_names)

random_index = random.randint(0,len(list_names) - 1)

print(f"{list_names[random_index]} is gonna pay :)")
