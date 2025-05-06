def es_alpha(caracter):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return caracter in alfabeto


def tipo_identificador(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si es el comienzo de una palabra o si el carácter actual no es alfabético
        if i == 0 or entrada[i-1] == ' ' or entrada[i-1] == '\n':
            if entrada[i] == '$':  # Verifica si el carácter actual es '$'
                inicio = i  # Guarda la posición inicial del identificador
                contador = 0  # Contador para el tamaño del identificador
                i += 1  # Avanza al siguiente carácter

                # Verifica si el siguiente carácter es alfabético y cuenta los caracteres del identificador
                if i < len(entrada) and es_alpha(entrada[i]):
                    contador += 1
                    i += 1

                    while i < len(entrada) and contador <= 10:
                        # Verifica si el carácter actual no es espacio o salto de línea y cuenta los caracteres
                        if entrada[i] == ' ' or entrada[i] == '\n':
                            break
                        contador += 1
                        i += 1
                    fin = i  # Guarda la posición final del identificador

                    # Verifica si el identificador cumple con las condiciones y está seguido por un espacio o salto de línea
                    if (i == len(entrada) or entrada[i] == ' ' or entrada[i] == '\n') and contador >= 2 and contador <= 10:
                        lexema = entrada[inicio:i]  # Extrae el identificador
                        # Agrega el identificador a la lista de lexemas
                        lexemas.append(
                            ('IDENTIFICADOR', lexema, inicio, fin - 1))
                    else:
                        while i < len(entrada) and entrada[i] != ' ':
                            i += 1  # Avanza hasta el siguiente espacio si el identificador no es válido
                else:
                    i += 1  # Avanza al siguiente carácter si no es un carácter alfabético
            else:
                i += 1  # Avanza al siguiente carácter si no es el inicio de un identificador
        else:
            i += 1  # Avanza al siguiente carácter si no es el inicio de una palabra

    if not lexemas:
        return []  # Si no se encontraron identificadores, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de lexemas encontrados
