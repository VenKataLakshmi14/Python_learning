import random


def guessing_game():
    secret_number = random.randint(1, 10)
    guess_limit = 3
    guess_count = 0  # Separate counter for valid guesses

    print("Welcome to the Guessing Game!")

    while guess_count < guess_limit:
        try:
            guess = int(input(f"Guess {guess_count + 1} : "))  # Prompt for a guess

            # Check if the guess is within the valid range 1 to 10
            if guess < 1 or guess > 10:
                print("Out of range. Please guess a number between 1 and 10.")
                continue

            # Increment count only for valid numeric guesses
            guess_count += 1

            # Compare the guess with the secret number
            if guess == secret_number:
                print("You won!")
                break
            else:
                print("Incorrect guess.")
        except ValueError:
            # Handle non-numeric input without incrementing the guess count
            print("Invalid input. Please enter a valid number.")

    else:
        # If all valid attempts are used without guessing correctly
        print(f"Sorry, you failed. The secret number was {secret_number}.")


# Run the game
guessing_game()