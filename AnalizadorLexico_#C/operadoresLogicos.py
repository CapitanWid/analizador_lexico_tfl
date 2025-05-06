def es_operador_logico(lexema):
    operadores_logicos = ['&&', '||']
    return lexema in operadores_logicos


def tipo_operador_logico(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    # Itera hasta el penúltimo carácter para verificar operadores de 2 caracteres
    while i < len(entrada) - 1:
        # Verifica si el segmento de 2 caracteres es un operador lógico
        if entrada[i:i+2] in ('&&', '||'):
            inicio = i  # Guarda la posición inicial del operador
            lexema = entrada[i:i+2]  # Extrae el operador completo
            # Agrega el operador a la lista de lexemas
            lexemas.append(('OPERADOR_LOGICO', lexema, inicio, inicio+1))
            # Avanza al siguiente par de caracteres (operador de 2 caracteres)
            i += 2
        else:
            i += 1  # Avanza al siguiente carácter si no es un operador lógico

    if not lexemas:
        return []  # Si no se encontraron operadores lógicos, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
