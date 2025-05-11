from token_modelo import Token, Categoria

class IdentificarIncrementoDecremento:
    OPERADORES = {"++", "--"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        for op in IdentificarIncrementoDecremento.OPERADORES:
            if codigo_fuente[indice:indice+2] == op:
                return Token(op, Categoria.OPERADOR_INCREMENTO,indice, indice + 2)
        return None
