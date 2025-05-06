def es_digito(caracter):
    digitos = "0123456789"
    return caracter in digitos


def es_alpha(caracter):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return caracter in alfabeto


def tipo_numero(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        # Verifica si es el comienzo de una palabra o si el carácter actual no es alfabético
        if i == 0 or not es_alpha(entrada[i-1]):
            if es_digito(entrada[i]):  # Comprueba si el carácter actual es un dígito
                inicio = i  # Guarda la posición inicial del número
                es_entero = True  # Bandera para identificar si es un número entero
                tiene_punto = False  # Bandera para identificar si el número tiene punto decimal

                while i < len(entrada) and (es_digito(entrada[i]) or entrada[i] == '.'):
                    if entrada[i] == '.':
                        es_entero = False  # Se cambia a falso si hay punto decimal
                        tiene_punto = True  # Marca que el número tiene punto decimal
                    i += 1  # Avanza al siguiente carácter

                fin = i  # Guarda la posición final del número

                # Verifica si el número está seguido por un espacio o si es el final de la cadena
                if i == len(entrada) or not es_alpha(entrada[i-1]):
                    lexema = entrada[inicio:fin]  # Extrae el número

                    if tiene_punto:
                        # Agrega número real a la lista de lexemas
                        lexemas.append(
                            ('NUMERO_REAL', lexema, inicio, fin - 1))
                    elif es_entero:
                        # Agrega número entero a la lista
                        lexemas.append(
                            ('NUMERO_ENTERO', lexema, inicio, fin - 1))
                else:
                    while i < len(entrada) and entrada[i] != ' ':
                        i += 1  # Avanza hasta el siguiente espacio o final de la cadena si el número no es válido
            else:
                i += 1  # Avanza al siguiente carácter si no es un dígito
        else:
            i += 1  # Avanza al siguiente carácter si no es el inicio de una palabra

    return lexemas  # Retorna la lista de lexemas encontrados
