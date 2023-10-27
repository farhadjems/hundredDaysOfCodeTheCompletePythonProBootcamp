

weight = float(input("Enter your wieght (kg): "))
height = float(input("Enter your height (m): "))

bmi = int(weight / height **2)
print(f"Your bmi is: {bmi}")

if bmi < 18.5:
    print("You are underwieght")
elif bmi < 25:
    print("You are normal")
elif bmi < 30: 
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")

