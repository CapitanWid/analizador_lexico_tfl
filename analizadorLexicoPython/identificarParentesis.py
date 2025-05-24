from token_modelo import Token, Categoria

class IdentificarParentesis:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] == '(':
            return Token('(', Categoria.PARENTESIS_APERTURA, indice, indice + 1)
        elif codigo_fuente[indice] == ')':
            return Token(')', Categoria.PARENTESIS_CIERRE, indice, indice + 1)
        return None