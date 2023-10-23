num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters")
#! since num_char is an int variable, it occurs error

#* to check data or variable type, use type() function
print(type(num_char))


# * to convert a variable to string, use str() function
#* to convert to int, use int()
#* to convert to float, use float()
print("Your name has " + str(num_char) + " characters")
print(70+ float("100.5"))
print(str(70)+str(100))