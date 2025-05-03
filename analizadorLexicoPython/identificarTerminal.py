from token_modelo import Token, Categoria

class IdentificarTerminal:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] == ";":
            return Token(";", Categoria.TERMINAL, indice + 1)
        return None
