# friendly program

name = input("What is your name?")
age = int(input("How old are you?"))
country = input("Which country do you live in?")

print("Hello", name, "from", country)

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")