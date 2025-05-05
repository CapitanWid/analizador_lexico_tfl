from token_modelo import Token, Categoria

class IdentificarComentarios:
    @staticmethod
    def extraer(codigo_fuente, indice):
        # Detecta comentario de una línea
        if codigo_fuente[indice:indice+2] == "//":
            inicio = indice
            while indice < len(codigo_fuente) and codigo_fuente[indice] != '\n':
                indice += 1
            return Token(codigo_fuente[inicio:indice], Categoria.COMENTARIO_LINEA, indice)

        # Detecta comentario de bloque (varias líneas)
        elif codigo_fuente[indice:indice+2] == "/*":
            inicio = indice
            indice += 2  # Avanzamos el índice después de "/*"

            # Buscamos el cierre del comentario "*/"
            while indice < len(codigo_fuente) and codigo_fuente[indice:indice+2] != "*/":
                indice += 1

            if indice < len(codigo_fuente):  # Aseguramos que encontremos el cierre "*/"
                indice += 2  # Avanzamos el índice después de "*/"
                return Token(codigo_fuente[inicio:indice], Categoria.COMENTARIO_BLOQUE, indice)
            else:
                # Si no se encuentra el cierre, consideramos todo hasta el final como comentario de bloque
                return Token(codigo_fuente[inicio:], Categoria.COMENTARIO_BLOQUE, len(codigo_fuente))

        return None