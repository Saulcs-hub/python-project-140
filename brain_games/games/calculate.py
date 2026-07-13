import random


from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
MAX_NUMBER = 50

def gerate_questions():
    numero_1 = random.randint(1, MAX_NUMBER)
    numero_2 = random.randint(1, MAX_NUMBER)

    operations = ["+", "-", "*"]
    operation = random.choice(operations)
    return numero_1, numero_2, operation

def calculate_answer(numero_1, numero_2, operation):
    if operation == "+":
        return numero_1 + numero_2
    elif operation == "-":
        return numero_1 - numero_2
    elif operation == "*":
        return numero_1 * numero_2

def play_brain_calculate():
    # Llamar a el name de la funcion welcome con la variable name
    name = welcome_user()
    print("What is the result of the expression?")


    contador = 0
    while contador < ROUNDS_TO_WIN:
        
        numero_1, numero_2, operation = gerate_questions()
        print(f"Question: {numero_1} {operation} {numero_2}")

        result = int(input("Your answer: "))
        correct_answer = calculate_answer(numero_1, numero_2, operation)

        if result == correct_answer:
            contador += 1
            print(f"Correct!")
        else:
            print(f"{result} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")