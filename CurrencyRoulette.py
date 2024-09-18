import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self._difficulty = None
        self.difficulty = difficulty
    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError("Difficulty must be an integer between 1 and 5")
        self._difficulty = value

    def get_money_interval(self):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        exchange_rate = response.json()
        rate = exchange_rate['rates']['ILS']
        t = random.randint(1, 100)
        interval = (t - (5 - self.difficulty), t + (5 - self.difficulty))
        return t, rate, interval

    def get_guess_from_user(self, t, rate):
        guess = float(input(f"Guess the value of {t} USD in ILS: "))
        return guess

    def play(self):
        t, rate, interval = self.get_money_interval()
        print(f"Exchange rate: 1 USD = {rate} ILS")
        guess = self.get_guess_from_user(t, rate)
        correct_value = t * rate
        if interval[0] <= guess <= interval[1]:
            print("Congratulations! Your guess is within the correct interval.")
            return True
        else:
            print(f"Sorry, the correct value was {correct_value:.2f} ILS.")
            return False

def play(difficulty):
    game = CurrencyRouletteGame(difficulty)
    return game.play()

if __name__ == '__main__':
    difficulty = 3
    result = play(difficulty)
    print("You won!" if result else "You lost!")