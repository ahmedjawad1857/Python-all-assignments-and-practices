# import pandas as pd

# s1 : pd.Series = pd.Series([1,2,3,4], name="student id")
# s2 : pd.Series = pd.Series([10,20,30,40], name="score")
# s3 : pd.Series = pd.Series(["John","Robert","David","Micheal"], name="student name")


# df1 : pd.DataFrame = pd.DataFrame({"student id":s1, "score":s2, "student name":s3})
# print(df1)


import random

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Set the number of attempts allowed
    max_attempts = 5
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        # Get the user's guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Increment the number of attempts
        attempts += 1

        # Display the number of attempts left
        attempts_left = max_attempts - attempts
        print(f"Attempts left: {attempts_left}")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Call the function to start the game
guess_the_number()
