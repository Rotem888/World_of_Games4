import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, 50)

    def get_guess_from_user(self):
        return int(input("Guess a number between 1 and 50: "))

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("Congratulations! You guessed the number.")
            return True
        else:
            print(f"Sorry, the number was {self.secret_number}.")
            return False

def play(difficulty):
    game = GuessGame(difficulty)
    return game.play()

if __name__ == "__main__":
    difficulty_level = 2
    result = play(difficulty_level)
    print("You won!" if result else "You lost!")