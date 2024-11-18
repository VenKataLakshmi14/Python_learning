import random

def guessing_game():
    secret_number = random.randint(1, 10)
    guess_limit = 3

    for guess_count in range(guess_limit):
        try:
            guess = int(input(f"Guess {guess_count + 1} : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < 1 or guess > 10:
            print("Out of range. Please guess a number between 1 and 10.")
            continue

        if guess == secret_number:
            print("You won!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print(f"Sorry, you failed. The secret number was {secret_number}.")

# Run the game
guessing_game()
