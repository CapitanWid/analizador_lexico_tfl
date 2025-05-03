# tokens/identificarEnteros.py

from token_modelo import Token, Categoria

class IdentificarEnteros:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
            posicion = indice
            while indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
                indice += 1

            # Validar que no esté seguido de punto (sería un decimal)
            if indice < len(codigo_fuente) and codigo_fuente[indice] == '.':
                return None

            return Token(codigo_fuente[posicion:indice], Categoria.ENTERO, indice)

        return None
