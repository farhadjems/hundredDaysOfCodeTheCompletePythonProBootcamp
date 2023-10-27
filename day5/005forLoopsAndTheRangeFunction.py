
#! note that range is inclusive-exclusive
for number in range (1, 10):
    print(number)

#* by default, the step is 1, to change the step, determine it as the 3rd argument

#! note that the loop variable stays defined after the loop, unlike C++ 
print (number)

sum_number = 0
for number in range(1,101):
    sum_number += number

print(sum_number)