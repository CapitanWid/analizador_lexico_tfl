from enum import Enum

class Categoria(Enum):
    NO_RECONOCIDO = 1
    ENTERO = 2
    DECIMAL = 3
    IDENTIFICADOR = 4
    PALABRA_RESERVADA = 5
    CADENA_CARACTERES = 6
    COMENTARIO_LINEA = 7
    COMENTARIO_BLOQUE = 8
    OPERADOR_ARITMETICO = 9
    OPERADOR_RELACIONAL = 10
    OPERADOR_LOGICO = 11
    OPERADOR_INCREMENTO = 12
    OPERADOR_ASIGNACION = 13  
    TERMINAL = 14  # categoría para fin de sentencia (;)
    SEPARADOR = 15  # categoría para separadores (coma, etc.)
    PARENTESIS_APERTURA = 16  
    PARENTESIS_CIERRE = 17  
    LLAVE_APERTURA = 18
    LLAVE_CIERRE = 19
    CORCHETE_APERTURA = 20
    CORCHETE_CIERRE = 21
    OPERADOR_COMPARACION = 22
    ERROR_CADENA_CARACTERES=23
    ERROR_COMENTARIO_BLOQUE=24


class Token:
    def __init__(self, palabra, categoria,indice_inicial, indice_sgte):
        self.palabra = palabra
        self.categoria = categoria
        self.indice_inicial = indice_inicial
        self.indice_sgte = indice_sgte

    def __repr__(self):
        return (f"Token(palabra={self.palabra}, categoria={self.categoria},"
                f"indice_inicial={self.indice_inicial},indice_sgte={self.indice_sgte})")