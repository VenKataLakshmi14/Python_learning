import random

secret_number = random.randint(1, 10)
guess_limit = 3

for guess_count in range(guess_limit):
    try:
        guess = int(input(f"Guess {guess_count + 1}: "))
    except ValueError:
        print("Invalid input.")
        continue

    if guess == secret_number:
        print("You won")
        break
else:
    print(f"Sorry, you failed. The secret number was {secret_number}.")
