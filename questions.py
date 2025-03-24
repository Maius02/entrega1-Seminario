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

# puntaje del jugador
score = 0.0

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]): # respuestas 
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):

        # leo respuesta
        user_answer = input("Respuesta: ")

        # verifico que lo ingresado sea valido
        if  not user_answer.isdigit() :
            print("Respuesta no valida.")
            sys.exit(1)
        user_answer = int(user_answer) - 1
        if not (0 <= user_answer <= 3): 
            print("Respuesta no valida.")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index[question_index]:
            score += 1 
            print("¡Correcto!")
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        score -= 0.5
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])
        
    # Se imprime un blanco al final de la pregunta
    print()
print(f'Puntaje:  {score}/3')