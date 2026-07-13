import random

from brain_games.cli import welcome_user

def play_brain_calculate():
    # Llamar a el name de la funcion welcome
    name = welcome_user()
    contador = 0
    while contador < 3:
        numero_1 = random.randint(1, 50)
        numero_2 = random.randint(1, 50)
        print("What is the result of the expression?")
        print(f"Question: {numero_1} + {numero_2}")
        result = int(input("Your answer: "))
        
        # Caso para la suma
        if result == numero_1 + numero_2:
            contador += 1
            print("Correct!")
        else:
            print(f"{result} is wrong answer ;(. Correct answer was {numero_1 + numero_2}.")
            print(f"Let's try again {name}!")
            return

        numero_1 = random.randint(1, 50)
        numero_2 = random.randint(1, 50)
        # Caso para la multiplicacion
        print(f"Question: {numero_1} * {numero_2}")
        result = int(input("Your answer: "))
        
        if result == numero_1 * numero_2:
            contador += 1
            print("Correct!")
        else:
            print(f"{result} is wrong answer ;(. Correct answer was {numero_1 * numero_2}.")
            print(f"Let's try again {name}!")
            return

        numero_1 = random.randint(1, 50)
        numero_2 = random.randint(1, 50)
        # Caso para la resta
        print(f"Question: {numero_1} - {numero_2}")
        result = int(input("Your answer: "))
        if result == numero_1 - numero_2:
            contador += 1
            print("Correct!")
        else:
            print(f"{result} is wrong answer ;(. Correct answer was {numero_1 - numero_2}.")
            print(f"Let's try again {name}!")
            return
    print(f"Congratulations, {name}!")