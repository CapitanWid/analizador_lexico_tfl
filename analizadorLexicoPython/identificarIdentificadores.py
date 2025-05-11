from token_modelo import Token, Categoria

class IdentificarIdentificadores:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice].isalpha() or codigo_fuente[indice] == '_':
            posicion = indice
            lexema = codigo_fuente[indice]
            indice += 1

           # while indice < len(codigo_fuente) and (codigo_fuente[indice].isalnum() or codigo_fuente[indice] == '_'):
            while indice < len(codigo_fuente) and len(lexema) < 10 and (codigo_fuente[indice].isalnum() or codigo_fuente[indice] == '_'):

                lexema += codigo_fuente[indice]
                indice += 1

            return Token(lexema, Categoria.IDENTIFICADOR,posicion, indice)
        return None
