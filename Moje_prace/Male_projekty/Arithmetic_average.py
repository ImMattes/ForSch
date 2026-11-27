grades = []
ones_and_twos = []
arithmetic_average_0 = 0

print("Enter a grade (1 - 5), or 0 to stop entering (For grades like 2- please enter 2.5).")

while True:
    grade = float(input("Enter a grade:"))
    if grade == 0 and grades:
        break
    elif grade == 0 and not grades:
        print("You have to enter at least one grade!")
    else:
        if grade not in (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5):
            print("Invalid grade!")
        else:
            grades.append(grade)
            if grade in (1, 1.5, 2, 2.5):
                ones_and_twos.append(grade)

print("Your grades:")

for grade in grades:
    print(grade)

print("Number of valid grades:", len(grades))
print("Number of ones and twos:", len(ones_and_twos))

for grade in grades:
    arithmetic_average_0 = arithmetic_average_0 + grade

arithmetic_average = arithmetic_average_0 / len(grades)

print("Arithmetic average of all grades:", arithmetic_average)

print("=====================")