from token_modelo import Token, Categoria

class IdentificarParentesis:
    SIMBOLOS = {"(", ")"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] in IdentificarParentesis.SIMBOLOS:
            return Token(codigo_fuente[indice], Categoria.PARENTESIS, indice + 1)
        return None
