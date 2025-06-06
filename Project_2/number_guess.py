import random

number_to_guess = random.randint(1, 100)

guess = -1
attempts = 0

while guess != number_to_guess:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1
    if attempts > 9:
        print("Game over! Better luck next time!")
        break
    if guess == number_to_guess:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")


