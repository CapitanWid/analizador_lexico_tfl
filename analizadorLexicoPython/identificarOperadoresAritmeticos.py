from token_modelo import Token, Categoria

class IdentificarOperadoresAritmeticos:
    OPERADORES = {"+", "-", "*", "/", "%"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] in IdentificarOperadoresAritmeticos.OPERADORES:
            return Token(codigo_fuente[indice], Categoria.OPERADOR_ARITMETICO,indice, indice + 1)
        return None
