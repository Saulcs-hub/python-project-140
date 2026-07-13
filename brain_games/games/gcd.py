import random
import math

from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
NUM_MAX = 50
def generate_questions():
    number_1 = random.randint(1, NUM_MAX)
    number_2 = random.randint(1, NUM_MAX)

    return number_1, number_2

def correct_answer(number_1, number_2):
    return math.gcd(number_1, number_2)

def play_brain_gcd():
    name = welcome_user()
    contador = 0

    print("Find the greatest common divisor of given numbers.")
    while contador < ROUNDS_TO_WIN:
        number_1, number_2 = generate_questions()
        print(f"Question: {number_1} {number_2}")

        result = int(input("Your answer: "))
        answer = correct_answer(number_1, number_2)

        if result == answer:
            contador += 1
            print("Correct!")
        else:
            print(f"{result} is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


