def es_operador_aritmetico(caracter):
    operadores_aritmeticos = ['+', '-', '*', '/', '%']
    return caracter in operadores_aritmeticos


def tipo_operador_aritmetico(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si el carácter actual es un operador aritmético
        if entrada[i] in ('+', '-', '*', '/', '%'):
            if (i+1) < len(entrada) and entrada[i+1] != '=' and (entrada[i+1] != '+' or entrada[i+1] != '-'):
                # Verifica si el siguiente carácter no es '=' y no es una secuencia de operadores '++' o '--'
                inicio = i  # Guarda la posición inicial del operador aritmético
                lexema = entrada[i]  # Extrae el operador aritmético
                # Agrega el operador a la lista de lexemas
                lexemas.append(('OPERADOR_ARITMETICO', lexema, inicio, inicio))
                i += 1
                break
            elif (i+1) == len(entrada):
                # Si el operador está al final de la cadena
                inicio = i
                lexema = entrada[i]
                lexemas.append(('OPERADOR_ARITMETICO', lexema, inicio, inicio))
                i += 1
            i += 1  # Avanza al siguiente carácter
        else:
            i += 1  # Avanza al siguiente carácter si no es un operador aritmético

    if not lexemas:
        return []  # Si no se encontraron operadores aritméticos, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
