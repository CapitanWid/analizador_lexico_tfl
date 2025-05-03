from token_modelo import Token, Categoria

class IdentificarLlaves:
    SIMBOLOS = {"{", "}"}

    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] in IdentificarLlaves.SIMBOLOS:
            return Token(codigo_fuente[indice], Categoria.LLAVE, indice + 1)
        return None
