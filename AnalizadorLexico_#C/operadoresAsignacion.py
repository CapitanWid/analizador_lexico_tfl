def es_operador_asignacion(lexema):
    operadores_asignacion = ['=', '+=', '-=', '*=', '/=']
    return lexema in operadores_asignacion


def tipo_operador_asignacion(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si el segmento de 2 caracteres es un operador de asignación compuesta
        if entrada[i:i+2] in ('+=', '-=', '*=', '/='):
            inicio = i  # Guarda la posición inicial del operador
            lexema = entrada[i:i+2]  # Extrae el operador completo
            # Agrega el operador a la lista de lexemas
            lexemas.append(('OPERADOR_ASIGNACION', lexema, inicio, inicio+1))
            # Avanza al siguiente par de caracteres (operador de 2 caracteres)
            i += 2
        elif entrada[i] == '=':  # Verifica si el carácter actual es '='
            # Verifica si el siguiente carácter no es '='
            if (i+1) < len(entrada) and entrada[i+1] != '=':
                # Verifica si el carácter anterior no es '='
                if (i-1) >= 0 and entrada[i-1] != '=':
                    inicio = i  # Guarda la posición inicial del operador
                    lexema = entrada[i]  # Extrae el operador '='
                    # Agrega el operador a la lista de lexemas
                    lexemas.append(
                        ('OPERADOR_ASIGNACION', lexema, inicio, inicio))
                    i += 1  # Avanza al siguiente carácter
                else:
                    i += 1  # Avanza al siguiente carácter si no se cumplen las condiciones
            # Verifica si el carácter anterior no es '='
            elif (i-1) >= 0 and entrada[i-1] != '=':
                inicio = i  # Guarda la posición inicial del operador
                lexema = entrada[i]  # Extrae el operador '='
                # Agrega el operador a la lista de lexemas
                lexemas.append(('OPERADOR_ASIGNACION', lexema, inicio, inicio))
                i += 1  # Avanza al siguiente carácter
            # Verifica si el operador '=' está al inicio o al final de la cadena
            elif i == 0 or i == len(entrada):
                inicio = i  # Guarda la posición inicial del operador
                lexema = entrada[i]  # Extrae el operador '='
                # Agrega el operador a la lista de lexemas
                lexemas.append(('OPERADOR_ASIGNACION', lexema, inicio, inicio))
                i += 1  # Avanza al siguiente carácter
            else:
                i += 1  # Avanza al siguiente carácter si no se cumplen las condiciones
        else:
            i += 1  # Avanza al siguiente carácter si no es un operador de asignación

    if not lexemas:
        return []  # Si no se encontraron operadores de asignación, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
