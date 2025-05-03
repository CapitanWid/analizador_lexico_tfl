from token_modelo import Token, Categoria

class IdentificarCadenaCaracteres:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] == '"':
            lexema = '"'
            i = indice + 1
            while i < len(codigo_fuente):
                if codigo_fuente[i] == '\\' and i + 1 < len(codigo_fuente):
                    lexema += codigo_fuente[i:i+2]
                    i += 2
                elif codigo_fuente[i] == '"':
                    lexema += '"'
                    return Token(lexema, Categoria.CADENA_CARACTERES, i + 1)
                else:
                    lexema += codigo_fuente[i]
                    i += 1
        return None
