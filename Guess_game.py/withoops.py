import random
from abc import ABC, abstractmethod

# Abstract base class
class Game(ABC):
    def __init__(self, min_num, max_num, guess_limit):
        self.min_num = min_num
        self.max_num = max_num
        self.guess_limit = guess_limit

    @abstractmethod
    def get_guess(self):
        # Abstract method to get a guess from the user
        pass

    @abstractmethod
    def check_guess(self, guess):
        # Abstract method to check the user's guess
        pass

class GuessingGame(Game):
    def __init__(self, min_num=1, max_num=10, guess_limit=3):
        super().__init__(min_num, max_num, guess_limit)
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.guess_count = 0
        
        

    def get_guess(self):
        while True:
            try:
                # Prompt the user to input their guess
                guess = int(input(f"Guess {self.guess_count + 1}: "))
                # Check if the guess is within the valid range
                if guess < self.min_num or guess > self.max_num:
                    print(f"Please guess a number between {self.min_num} and {self.max_num}.")
                else:
                    return guess
            except ValueError:
                # Handle invalid (non-numeric) input
                print("Invalid input. Please enter a valid number.")

    def check_guess(self, guess):
        if guess == self.secret_number:
            print("Congratulations! You guessed the correct number!")
            return True
        else:
            print("Incorrect guess.")
            return False

# Main program execution
if __name__ == "__main__":
    # Create an instance of GuessingGame
    game = GuessingGame()
    print("\nWelcome to the Guessing Game!")
    
    # Allow the user a certain number of attempts to guess the number
    for i in range(game.guess_limit):
        # Get a guess from the user
        guess = game.get_guess()
        game.guess_count += 1
        if game.check_guess(guess):
            break
    else:
        print(f"\nSorry, you didn't guess the number. The secret number was {game.secret_number}.\n")
