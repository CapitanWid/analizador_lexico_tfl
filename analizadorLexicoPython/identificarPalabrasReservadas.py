from token_modelo import Token, Categoria

class IdentificarPalabrasReservadas:
    PALABRAS = {"class", "void", "int", "string", "if", "else", "while", "return", "for"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        for palabra in IdentificarPalabrasReservadas.PALABRAS:
            fin = indice + len(palabra)
            if codigo_fuente[indice:fin] == palabra:
                if fin == len(codigo_fuente) or not codigo_fuente[fin].isalnum():
                    return Token(palabra, Categoria.PALABRA_RESERVADA, fin)
        return None
