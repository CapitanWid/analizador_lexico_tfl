from token_modelo import Token, Categoria

class IdentificarComentarios:
    @staticmethod
    def extraer(codigo_fuente, indice):
        # Comentario de una línea
        if codigo_fuente[indice:indice+2] == "//":
            inicio = indice
            while indice < len(codigo_fuente) and codigo_fuente[indice] != '\n':
                indice += 1
            return Token(codigo_fuente[inicio:indice], Categoria.COMENTARIO_LINEA, inicio, indice)

        # Comentario de bloque
        elif codigo_fuente[indice:indice+2] == "/*":
            inicio = indice
            indice += 2

            while indice < len(codigo_fuente) and codigo_fuente[indice:indice+2] != "*/":
                indice += 1

            if indice < len(codigo_fuente) - 1:
                indice += 2  # consumimos el "*/"
                return Token(codigo_fuente[inicio:indice], Categoria.COMENTARIO_BLOQUE, inicio, indice)
            else:
                # No se encontró cierre de comentario
                return Token(codigo_fuente[inicio:], Categoria.ERROR_COMENTARIO_BLOQUE, inicio, len(codigo_fuente))

        return None
