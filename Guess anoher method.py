secret_number = 5
guess_limit = 3

for guess_count in range(guess_limit):
    while True:
        try:
            guess = int(input(f"Guess {guess_count + 1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed.")
