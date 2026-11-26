# Secret Number Program

import random

while True:
    
    secret_number = random.randint(1, 100)
    guess = 0
    number_of_attempts = 0

    while guess != secret_number:

        guess = int(input("Guess a random number between 1 and 100:"))

        if guess > secret_number:
            print ("The secret number is smaller.")
        elif guess < secret_number:
            print ("The secret number is bigger.")

        number_of_attempts = number_of_attempts + 1

    if guess == secret_number:
        print ("Good job, you guessed the secret number on your", number_of_attempts, "attempt")

    answer = input("Do you want to play again?")
    if answer == "no":
        print ("Ok.")
        break
    print("=====================")