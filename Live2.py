import MemoryGame
import GuessGame
import CurrencyRoulette


def welcome():
    name = input("Enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")
    return name

def load_game():
    while True:
        user_input = int(input("Please choose a game to play between 1-3 (or 0 to exit): "))
        if user_input == 0:
            print("Thank you for playing! Goodbye!")
            break

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
        else:
            print("Invalid choice")
            continue

        if result:
            print("You won!")
        else:
            print("You lost!")

def difficulty():
    while True:
        num = int(input("Please choose game difficulty from 1 to 3: "))
        if 1 <= num <= 3:
            print(f"The game difficulty is: {num}")
            return num
        else:
            print("Invalid difficulty level, please try again")

welcome()
load_game()