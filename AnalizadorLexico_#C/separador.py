def es_separador(caracter):
    # Función para verificar si un carácter es una coma ','
    return caracter == ','


def tipo_separador(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        if es_separador(entrada[i]):  # Verifica si el carácter actual es una coma
            inicio = i  # Guarda la posición inicial de la coma
            lexema = entrada[i]  # Extrae la coma
            # Agrega la coma a la lista de lexemas
            lexemas.append(('SEPARADOR', lexema, inicio, inicio))
            i += 1  # Avanza al siguiente carácter
        else:
            i += 1  # Avanza al siguiente carácter si no es una coma

    if not lexemas:
        return []  # Si no se encontraron comas, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de comas encontradas
