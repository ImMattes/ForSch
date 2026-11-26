grades = []
grade = ("anything")
ones_and_twos = []
Arithmetic_average_0 = 0

print("Enter a grade (1 - 5), or 0 to stop entering.")

while True:
    grade = int(input("Enter a grade:"))
    if grade == 0:
        break
    if grade < 1 or grade > 5:
        print("Invalid grade!")
    else:
        grades.append(grade)
        if grade == 1 or grade == 2:
            ones_and_twos.append(grade)

print("Your grades:")

for grade_ in grades:
    print(grade_)

print("Number of valid grades:", len(grades))
print("Number of ones and twos:", len(ones_and_twos))

for grade__ in grades:
    Arithmetic_average_0 = Arithmetic_average_0 + grade__

Arithmetic_average = Arithmetic_average_0 / len(grades)

print("Arithmetic average of all grades:", Arithmetic_average)

print("=====================")