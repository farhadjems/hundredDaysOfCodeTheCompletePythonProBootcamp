import random

#* to generate a random int between a and b (both inclusive): random.ranint(a,b)
random_integer = random.randint(1,10)
print(random_integer)
#* to import an implemented module:
import my_module
print(my_module.pi)

#* to generate a random float number between 0 and 1
random_float = random.random()
print(random_float)

#* to generate a random number between a and b: a + (b-a) * random.random()
random_number = random.random() * (5) + 5
print(random_number)