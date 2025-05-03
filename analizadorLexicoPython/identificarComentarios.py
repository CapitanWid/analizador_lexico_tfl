from token_modelo import Token, Categoria

class IdentificarComentarios:
    @staticmethod
    def extraer(codigo_fuente, indice):
        if codigo_fuente[indice:indice+2] == "//":
            inicio = indice
            while indice < len(codigo_fuente) and codigo_fuente[indice] != '\n':
                indice += 1
            return Token(codigo_fuente[inicio:indice], Categoria.COMENTARIO_LINEA, indice)

        elif codigo_fuente[indice:indice+2] == "/*":
            inicio = indice
            indice += 2
            while indice < len(codigo_fuente) and codigo_fuente[indice:indice+2] != "*/":
                indice += 1
            if indice < len(codigo_fuente):
                indice += 2
                return Token(codigo_fuente[inicio:indice], Categoria.COMENTARIO_BLOQUE, indice)
        return None
