
print("Welcome to the tip calculator")
bill = input("What was the total bill?$ ")
tip_percentage = input("What percentage tipe would you like to give? 10, 12, or 15? ")
number_people=input("How many people to split the bill? ")

# converting inputs to appropriate types
bill = float(bill)
tip_percentage = int(tip_percentage) / 100 # to make it as percent
number_people = int(number_people)

# calculating the total cost
total_bill = bill * (1+tip_percentage)
each_share = total_bill / number_people

each_share = round(each_share, 2)
# to force the print function to print with 2 decimals
each_share = "{:.2f}".format(each_share)

meassge = f"Each person should pay ${each_share}"
print(meassge)