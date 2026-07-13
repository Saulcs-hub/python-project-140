import random
from brain_games.cli import welcome_user


def play_brain_even():
    # Ejecutamos la funcion y nos devuelve la variable name
    name = welcome_user()

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    # Agregando contador
    contador = 0
    while contador < 3:
        # Usamos la libreria standar de random para generar valores entre 0 y 50
        number = random.randint(0, 50)

        # Preguntamos al usuario si el numero que ve es par o no
        print(f"Question: {number}")

        # Guardamos la respuesta de usuario
        answer = input("Your answer: ")

        # Validar que sea una respuesta valida
        if not answer and isinstance(answer, str):
            break

        # Logica del juego
        # Validacion de respuestas si son correctas

        if answer == "yes" and number % 2 == 0:
            print("Correct!")
            contador += 1
        elif answer == "no" and number % 2 != 0:
            print("Correct!")
            contador += 1

        # Validacion si las respuestas son incorrectas
        elif answer == "yes" and number % 2 != 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return
        elif answer == "no" and number % 2 == 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return

    # Si el bucle termina las 3 respuestas fueron correctas
    print(f"Congratulations, {name}!")
