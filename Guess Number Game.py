import random

number_to_guess = random.randint(1, 100)
attempts = 0  
print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Try to guess it!")

while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low! Try a higher number.")
    elif user_guess > number_to_guess:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  
