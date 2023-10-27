student_score = input("Enter a list of student score: ").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

max_score = 0
for score in student_score: 
    if score > max_score:
        max_score = score

print(f"The max score is: {max_score}")