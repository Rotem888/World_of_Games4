import GuessGame
import CurrencyRoulette
import MemoryGame
from Score import add_score

def welcome():
    name = input("Enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")
    return name

def load_game():
    while True:
        try:
            user_input = int(input("Please choose a game to play between 1-3 (or 0 to exit): "))
            if user_input == 0:
                print("Thank you for playing! Goodbye!")
                break
            elif user_input not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, 3, or 0 to exit.")
                continue

            difficulty_level = difficulty()

            if user_input == 1:
                print("Starting Memory Game...")
                result = MemoryGame.play(difficulty_level)
            elif user_input == 2:
                print("Starting Guess Game...")
                result = GuessGame.play(difficulty_level)
            elif user_input == 3:
                print("Starting Currency Roulette Game...")
                result = CurrencyRoulette.play(difficulty_level)

            if result:
                print("You won!")
                new_score = add_score(difficulty_level)
                print(f"Your new score is: {new_score}")
            else:
                print("You lost!")
        except ValueError:
            print("Invalid input. Please enter a number.")

def difficulty():
    while True:
        try:
            num = int(input("Please choose game difficulty from 1 to 3: "))
            if 1 <= num <= 3:
                print(f"The game difficulty is: {num}")
                return num
            else:
                print("Invalid difficulty level, please try again")
        except ValueError:
            print("Invalid input. Please enter a number.")

welcome()
load_game()