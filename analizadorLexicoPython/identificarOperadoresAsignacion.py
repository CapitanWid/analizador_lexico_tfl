from token_modelo import Token, Categoria

class IdentificarOperadoresAsignacion:
    OPERADORES = {"=", "+=", "-=", "*=", "/=", "%=", "&=", "^=", "|=", ">>=", "<<="}

    @staticmethod
    def extraer(codigo_fuente, indice):
        for op in sorted(IdentificarOperadoresAsignacion.OPERADORES, key=len, reverse=True):
            if codigo_fuente[indice:indice+len(op)] == op:
                return Token(op, Categoria.OPERADOR_ASIGNACION,indice, indice + len(op))
        return None
