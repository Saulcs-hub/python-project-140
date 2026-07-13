import random

from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
MAX_NUMBER = 100


def is_prime(number):
    # 1 no es primo
    if number < 2:
        return False

    # 2 es primo
    if number == 2:
        return True

    # Los pares no son primos
    if number % 2 == 0:
        return False

    # Verificar divisibilidad hasta la raíz cuadrada
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True


def get_correct_answer(number):
    return "yes" if is_prime(number) else "no"


def play_brain_prime():
    name = welcome_user()
    contador = 0

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while contador < ROUNDS_TO_WIN:
        number = random.randint(2, MAX_NUMBER)
        print(f"Question: {number}")

        answer = input("Your answer: ").strip()
        correct_answer = get_correct_answer(number)

        if answer == correct_answer:
            contador += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
