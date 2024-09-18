import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 50) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        print(f"Enter {self.difficulty} numbers (1-50) separated by spaces:")
        return list(map(int, input().split()))[:self.difficulty]

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play_game(self):
        sequence = self.generate_sequence()
        print("Remember these numbers:")
        print(*sequence)
        time.sleep(0.7)

        print("\n" * 100)
        print("Numbers have been cleared. Try to recall them!")

        user_sequence = self.get_list_from_user()
        return self.is_list_equal(sequence, user_sequence)

def play(difficulty):
    game = MemoryGame(difficulty)
    return game.play_game()

if __name__ == "__main__":
    difficulty = 3
    result = play(difficulty)
    print("You won!" if result else "You lost!")