from token_modelo import Token, Categoria

class IdentificarOperadoresLogicos:
    OPERADORES = {"&&", "||", "!", "&", "|", "^"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        for op in sorted(IdentificarOperadoresLogicos.OPERADORES, key=len, reverse=True):
            if codigo_fuente[indice:indice+len(op)] == op:
                return Token(op, Categoria.OPERADOR_LOGICO, indice, indice + len(op))
        return None