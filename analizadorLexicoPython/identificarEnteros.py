from token_modelo import Token, Categoria

class IdentificarEnteros:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
            inicio = indice
            while indice < len(codigo_fuente) and codigo_fuente[indice].isdigit():
                indice += 1

            # Validar que no esté seguido de punto (sería un número real)
            if indice < len(codigo_fuente) and codigo_fuente[indice] == '.':
                return None

            lexema = codigo_fuente[inicio:indice]
            return Token(lexema, Categoria.ENTERO, inicio, indice)

        return None
