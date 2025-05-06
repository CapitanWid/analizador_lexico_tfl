def es_llave(caracter):
    return caracter in ['{', '}']


def tipo_llave(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si el carácter actual es una llave '{' o '}'
        if es_llave(entrada[i]):
            inicio = i  # Guarda la posición inicial de la llave
            lexema = entrada[i]  # Extrae el carácter de la llave
            # Agrega la llave a la lista de lexemas
            lexemas.append(('LLAVE', lexema, inicio, inicio))
            i += 1  # Avanza al siguiente carácter
        else:
            i += 1  # Avanza al siguiente carácter si no es una llave

    if not lexemas:
        return []  # Si no se encontraron llaves, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
