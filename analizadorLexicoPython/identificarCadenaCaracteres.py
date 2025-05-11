from token_modelo import Token, Categoria

class IdentificarCadenaCaracteres:
    ESCAPES_VALIDOS = {'n', 't', 's', 'r'}

    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice] == '"':
            lexema = '"'
            i = indice + 1
            error = False

            while i < len(codigo_fuente):
                if codigo_fuente[i] == '\\':
                    if i + 1 < len(codigo_fuente):
                        siguiente = codigo_fuente[i + 1]
                        lexema += '\\' + siguiente
                        i += 2
                        if siguiente not in IdentificarCadenaCaracteres.ESCAPES_VALIDOS:
                            error = True
                            break
                    else:
                        lexema += '\\'
                        i += 1
                        error = True
                        break
                elif codigo_fuente[i] == '"':
                    lexema += '"'
                    return Token(lexema, Categoria.CADENA_CARACTERES, indice, i + 1)
                else:
                    lexema += codigo_fuente[i]
                    i += 1

            # Si salimos del while sin encontrar una comilla de cierre, o por error
            # Continuar hasta el cierre o final del archivo
            while i < len(codigo_fuente) and codigo_fuente[i] != '"':
                lexema += codigo_fuente[i]
                i += 1
            if i < len(codigo_fuente) and codigo_fuente[i] == '"':
                lexema += '"'
                i += 1

            return Token(lexema, Categoria.ERROR_CADENA_CARACTERES, indice, i)

        return None
