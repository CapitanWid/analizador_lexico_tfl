from token_modelo import Token, Categoria

class IdentificarSeparador:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] == ",":
            return Token(",", Categoria.SEPARADOR,indice, indice + 1)
        return None
