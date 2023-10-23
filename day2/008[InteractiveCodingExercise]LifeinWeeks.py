
age = input("What is your current age? ")

age = int(age)
final_age = 90

age_left = final_age - age
month_left = age_left * 12
week_left = age_left * 52
day_left = week_left * 7

message = f"You have {day_left} days, {week_left} weeks, and {month_left} months left."

print(message)