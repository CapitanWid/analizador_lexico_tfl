def tipo_comentarios(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada) - 1:
        # Comentario de línea
        if entrada[i:i+2] == '//':  # Verifica si encuentra el inicio de un comentario de línea
            inicio = i  # Guarda la posición inicial del comentario
            # Busca la posición del salto de línea o fin del comentario
            fin = entrada.find('\n', inicio + 2)
            if fin == -1:
                # Si no hay salto de línea, el comentario llega hasta el final del texto
                fin = len(entrada) - 1
            lexema = entrada[inicio:fin]  # Extrae el comentario de línea
            # Agrega el comentario a la lista de lexemas
            lexemas.append(('COMENTARIO_LINEA', lexema, inicio, fin))
            i = fin  # Actualiza el índice para continuar después del comentario
        # Comentario de bloque
        elif entrada[i:i+2] == '/*':  # Verifica si encuentra el inicio de un comentario de bloque
            inicio = i  # Guarda la posición inicial del comentario de bloque
            # Busca el cierre del comentario de bloque
            fin = entrada.find('*/', inicio + 2)
            if fin == -1:
                # Si no hay cierre, el comentario llega hasta el final del texto
                fin = len(entrada) - 1
            lexema = entrada[inicio:fin+2]  # Extrae el comentario de bloque
            # Agrega el comentario a la lista de lexemas
            lexemas.append(('COMENTARIO_BLOQUE', lexema, inicio, fin+1))
            i = fin + 2  # Actualiza el índice para continuar después del comentario de bloque
        else:
            i += 1  # Avanza al siguiente carácter si no es el inicio de un comentario

    if not lexemas:
        return []  # Si no se encontraron comentarios, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
