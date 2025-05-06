def es_operador_comparacion(lexema):
    operadores_comparacion = ['==', '!=', '<=', '>=', '<', '>']
    return lexema in operadores_comparacion


def tipo_operador_comparacion(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    # Itera hasta el penúltimo carácter para verificar operadores de 2 caracteres
    while i < len(entrada) - 1:
        # Verifica si el segmento de 2 caracteres es un operador de comparación de 2 caracteres
        if entrada[i:i+2] in ('==', '!=', '<=', '>='):
            inicio = i  # Guarda la posición inicial del operador
            lexema = entrada[i:i+2]  # Extrae el operador completo
            # Agrega el operador a la lista de lexemas
            lexemas.append(('OPERADOR_COMPARACION', lexema, inicio, inicio+1))
            # Avanza al siguiente par de caracteres (operador de 2 caracteres)
            i += 2
        elif entrada[i] in ('<', '>'):  # Verifica si el carácter actual es '<' o '>'
            inicio = i  # Guarda la posición inicial del operador
            lexema = entrada[i]  # Extrae el operador '<' o '>'
            # Agrega el operador a la lista de lexemas
            lexemas.append(('OPERADOR_COMPARACION', lexema, inicio, inicio))
            i += 1  # Avanza al siguiente carácter
        else:
            i += 1  # Avanza al siguiente carácter si no es un operador de comparación

    if not lexemas:
        return []  # Si no se encontraron operadores de comparación, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
