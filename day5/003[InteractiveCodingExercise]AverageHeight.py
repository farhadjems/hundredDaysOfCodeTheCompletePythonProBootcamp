student_heights = input("Enter a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_height = 0
number_students = 0
for student in student_heights:
    sum_height += student
    number_students += 1

average_height = sum_height / number_students
average_height = round(average_height)

print (f"Average of heights is: {average_height}")