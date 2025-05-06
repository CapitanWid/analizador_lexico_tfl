def es_hexadecimal(caracter):
    return caracter.isdigit() or ('A' <= caracter.upper() <= 'F')


def tipo_hexadecimales(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    # Itera hasta los últimos 6 caracteres para verificar el formato del hexadecimal
    while i < len(entrada) - 6:
        if (
            entrada[i] == '#' and  # Verifica si el carácter es '#'
            # Verifica si los siguientes 6 caracteres son hexadecimales
            all(es_hexadecimal(entrada[j]) for j in range(i + 1, i + 7)) and
            # Verifica si el siguiente carácter después del hexadecimal no es alfanumérico
            not entrada[i + 7].isalnum()
        ):
            inicio = i  # Guarda la posición inicial del hexadecimal
            fin = i + 6  # Guarda la posición final del hexadecimal
            # Extrae el lexema completo del hexadecimal
            lexema = entrada[inicio:fin + 1]
            # Agrega el lexema a la lista de lexemas
            lexemas.append(('HEXADECIMAL', lexema, inicio, fin))
            i = fin + 1  # Actualiza el índice para continuar después del lexema hexadecimal
        else:
            i += 1  # Avanza al siguiente carácter si no se encontró un formato de hexadecimal

    if not lexemas:
        return []  # Si no se encontraron hexadecimales, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
