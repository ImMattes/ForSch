# friendly program

Name = input("What is your name?")
Age = int(input("How old are you?"))
Country = input("Which country do you live in?")

print("Hello", Name, "from", Country)

if Age > 18:
    print("You are an adult")
else:
    print("You are not an adult")