from token_modelo import Token, Categoria

class IdentificarReales:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice].isdigit():
            posicion = indice
            while indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
                indice += 1

            if indice < len(codigo_fuente) and codigo_fuente[indice] == '.':
                indice += 1
                if indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
                    while indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
                        indice += 1
                    return Token(codigo_fuente[posicion:indice], Categoria.DECIMAL, posicion, indice)
        return None
