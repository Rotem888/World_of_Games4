def welcome():
    name = input("Enter your name:")
    return name

print("Hello" + " " + welcome() + " " "and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
def load_game():
    user = int(input("Please choose a game to play between 1-3:"))
    if user == 1:
        print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    elif user == 2:
        print("Guess Game - guess a number and see if you chose like the computer")
    elif user == 3:
        print("Currency Roulette - try and guess the value of a random amount of USD in ILS")
    else:
        print("Invalid choice")

def difficulty():
    num  = int(input("Please choose game difficulty from 1 to 5:"))
    if 1 <= num <= 5:
        print("The game difficulty is:", num)
    else:
        print("The game will not work, please try again")

load_game()
difficulty()
exit()