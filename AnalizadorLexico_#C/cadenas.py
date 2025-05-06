def tipo_cadenas(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si se encuentra una comilla doble para identificar el inicio de una cadena
        if entrada[i] == '"':
            inicio = i  # Guarda la posición inicial de la cadena
            # Busca la posición del cierre de comillas
            fin = entrada.find('"', inicio + 1)

            if fin == -1:
                # Si no se encuentra el cierre de comillas, se considera un error
                return [('ERROR_CIERRE_INCORRECTO', entrada, inicio, len(entrada) - 1)]

            # Extrae el lexema completo, incluyendo las comillas
            lexema = entrada[inicio:fin + 1]
            # Agrega el lexema a la lista
            lexemas.append(('CADENA', lexema, inicio, fin))
            i = fin + 1  # Actualiza el índice para continuar después del cierre de comillas
        else:
            i += 1  # Avanza al siguiente carácter si no es el inicio de una cadena

    if not lexemas:
        return []  # Si no se encontraron cadenas, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
