def es_palabra_reservada(lexema):
    # Lista de palabras reservadas
    palabras_reservadas = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander',
                           'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise']
    return lexema in palabras_reservadas


def es_alpha(caracter):
    # Función para verificar si un carácter es una letra del alfabeto
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return caracter in alfabeto


def tipo_palabra_reservada(entrada):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    i = 0  # Variable de índice para recorrer la cadena de entrada

    while i < len(entrada):
        if es_alpha(entrada[i]):  # Verifica si el carácter actual es una letra
            inicio = i  # Guarda la posición inicial de la palabra reservada
            contador = 0

            while i < len(entrada):
                if entrada[i] == ' ' or entrada[i] == '\n':
                    break  # Si encuentra un espacio o salto de línea, termina el reconocimiento de la palabra
                contador += 1
                i += 1
            fin = i  # Guarda la posición final de la palabra reservada

            lexema = entrada[inicio:fin]  # Extrae la palabra reservada

            # Verifica si la palabra es una palabra reservada conocida
            if es_palabra_reservada(lexema):
                # Agrega la palabra reservada a la lista de lexemas
                lexemas.append(('PALABRA_RESERVADA', lexema, inicio, fin - 1))
        else:
            i += 1  # Avanza al siguiente carácter si no es una letra

    if not lexemas:
        return []  # Si no se encontraron palabras reservadas, retorna una lista vacía
    else:
        return lexemas  # Retorna la lista de palabras reservadas encontradas
