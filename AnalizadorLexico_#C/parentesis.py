def es_parentesis(caracter):
    # Función para verificar si un carácter es un paréntesis '(' o ')'
    return caracter in ['(', ')']


def tipo_parentesis(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si el carácter actual es un paréntesis
        if es_parentesis(entrada[i]):
            inicio = i  # Guarda la posición inicial del paréntesis
            lexema = entrada[i]  # Extrae el paréntesis
            # Agrega el paréntesis a la lista de lexemas
            lexemas.append(('PARENTESIS', lexema, inicio, inicio))
            i += 1  # Avanza al siguiente carácter
        else:
            i += 1  # Avanza al siguiente carácter si no es un paréntesis

    if not lexemas:
        return []  # Si no se encontraron paréntesis, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de paréntesis encontrados
