from token_modelo import Token, Categoria

class IdentificarCorchetes:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] == '[':
            return Token('[', Categoria.CORCHETE_APERTURA, indice, indice + 1)
        elif codigo_fuente[indice] == ']':
            return Token(']', Categoria.CORCHETE_CIERRE, indice, indice + 1)
        return None