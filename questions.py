import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# devuelve una lista con 3 tuplas, que contienen [(question, answers, correct_answers_index)..]
questions_to_ask = random.sample( list( zip( questions, answers, correct_answers_index)), k=3)

# puntaje del jugador
score = 0.0

# El usuario deberá contestar 3 preguntas
for question, choices, correct_index in questions_to_ask:

    # Se muestra en pantalla la pregunta y las respuestas posibles
    print(question)     #imprime pregunta
    for i, choice in enumerate(choices): #imprime las respuests posibles
        print(f'{i+1}- {choice}')

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):

        # leo respuesta
        user_answer = input("Respuesta: ")

        # verifico que lo ingresado sea valido
        if  not user_answer.isdigit() or not( 1 <= int(user_answer) <= 4):
            print("Respuesta no valida.")
            sys.exit(1)

        # ajusto índice
        user_answer = int(user_answer) - 1

        # Si es correcta paso a la siguiente
        if user_answer == correct_index:
            score += 1      #suma puntos
            print("¡Correcto!")
            break
        else:
            print("Incorrecto.")
            score -= 0.5
    else:
        # el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        print(f'La respuesta correcta es: {choices[correct_index]} ')
        
    # Se imprime un blanco al final de la pregunta
    print()

#muestro puntaje obtenido
print(f'Puntaje:  {score}/3') 
