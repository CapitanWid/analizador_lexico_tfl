def es_operador_incremento_decremento(lexema):
    operadores_incremento_decremento = ['++', '--']
    return lexema in operadores_incremento_decremento


def tipo_operador_incremento_decremento(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    # Itera hasta el penúltimo carácter para verificar operadores de 2 caracteres
    while i < len(entrada) - 1:
        # Verifica si el segmento de 2 caracteres es un operador de incremento/decremento
        if entrada[i:i+2] in ('++', '--'):
            inicio = i  # Guarda la posición inicial del operador
            lexema = entrada[i:i+2]  # Extrae el operador completo
            # Agrega el operador a la lista de lexemas
            lexemas.append(('OPERADOR_INC_DEC', lexema, inicio, inicio+1))
            # Avanza al siguiente par de caracteres (operador de 2 caracteres)
            i += 2
        else:
            i += 1  # Avanza al siguiente carácter si no se encontró un operador

    if not lexemas:
        return []  # Si no se encontraron operadores de incremento/decremento, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
