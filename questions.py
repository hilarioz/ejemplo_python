import random
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
# Puntaje del usuario al iniciar
puntaje = 0
# Se genera la muestra de 3 preguntas distintas
question_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se muestra la pregunta y las respuestas posibles
    print(question_to_ask[_][0])
    for i, answer in enumerate(question_to_ask[_][1]):
        print(f"{i+1}.{answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_input = input("Respuesta: ")
        #Se verifica la validez de la entrada
        if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4":
            user_answer = int(user_input) - 1
            # Se verifica si la respuesta es correcta
            if user_answer == question_to_ask[_][2]:
                puntaje += 1
                print("¡Correcto!")
                break
            else:
                puntaje -= 0.5
        else:
            print("Respuesta no válida")
            exit(1)
    # Si el usuario no responde correctamente después de 2 intentos se muestra la respuesta correcta
    else:
        print("Incorrecto. La respuesta correcta es la numero:")
        print(enumerate(question_to_ask[_][2])[question_to_ask[_][2]])
    # Se imprime un blanco al final de la pregunta
    print()
print(f"Puntaje final: {puntaje}")
