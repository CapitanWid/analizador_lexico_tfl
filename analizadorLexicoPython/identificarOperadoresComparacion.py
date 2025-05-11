from token_modelo import Token, Categoria

class IdentificarOperadoresComparacion:
    OPERADORES = {"==", "!=", ">=", "<=", ">", "<"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        for op in sorted(IdentificarOperadoresComparacion.OPERADORES, key=len, reverse=True):
            if codigo_fuente[indice:indice+len(op)] == op:
                return Token(op, Categoria.OPERADOR_COMPARACION,indice, indice + len(op))
        return None
