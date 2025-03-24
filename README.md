# MAIA PAEZ 21151/3

#### Modifique el juego para, en lo posible, no acceder a las 3 listas usando índices.

Ayuda: questions_to_ask = random.choices( list( zip( questions, answers, correct_answers_index ) ), k=3 )

✅ En lugar de acceder a las listas questions, answers y correct_answers_index con índices, usamos zip() para crear una lista de tuplas donde cada elemento contiene (pregunta, respuestas, índice_correcto).
✅ Seleccionamos 3 preguntas aleatorias con random.choices(), en lugar de elegir índices manualmente con random.randint().

#### random.choices(lista, k=n) → Puede repetir elementos (con reemplazo).

#### random.sample(lista, k=n) → No repite elementos (sin reemplazo). SIRVE PARA N REPETIR PREGUNTAS
