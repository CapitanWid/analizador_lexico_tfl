def es_terminal(caracter):
    # Función para verificar si un carácter es un punto y coma ';'
    return caracter == ';'


def tipo_terminal(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si el carácter actual es un punto y coma
        if es_terminal(entrada[i]):
            inicio = i  # Guarda la posición inicial del punto y coma
            lexema = entrada[i]  # Extrae el punto y coma
            # Agrega el punto y coma a la lista de lexemas
            lexemas.append(('TERMINAL', lexema, inicio, inicio))
            i += 1  # Avanza al siguiente carácter
        else:
            i += 1  # Avanza al siguiente carácter si no es un punto y coma

    if not lexemas:
        return []  # Si no se encontraron puntos y coma, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de puntos y coma encontrados
