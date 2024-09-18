import os

SCORES_FILE_NAME = "Scores.txt"

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5

    try:
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + points_of_winning

    with open(SCORES_FILE_NAME, "w") as file:
        file.write(str(new_score))

    return new_score