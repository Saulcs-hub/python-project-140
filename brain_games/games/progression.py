import random

from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
PROGRESSION_LENGTH_MIN = 5
PROGRESSION_LENGTH_MAX = 10
MAX_FIRST_NUMBER = 100
MAX_STEP = 10


def generate_progression():
    # Longitud aleatoria entre 5 y 10
    length = random.randint(PROGRESSION_LENGTH_MIN, PROGRESSION_LENGTH_MAX)

    first_number = random.randint(1, MAX_FIRST_NUMBER)
    step = random.randint(1, MAX_STEP)

    progression = [first_number + step * i for i in range(length)]

    missing_position = random.randint(0, length - 1)
    missing_number = progression[missing_position]

    progression[missing_position] = ".."

    return progression, missing_number, missing_position


def format_progression(progression):
    return " ".join(str(num) for num in progression)


def play_brain_progression():
    name = welcome_user()
    contador = 0

    print("What number is missing in the progression?")

    while contador < ROUNDS_TO_WIN:
        progression, missing_number, _ = generate_progression()
        print(f"Question: {format_progression(progression)}")

        result = int(input("Your answer: "))

        if result == missing_number:
            contador += 1
            print("Correct!")
        else:
            print(
                f"'{result}' is wrong answer ;(. Correct answer was '{missing_number}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
