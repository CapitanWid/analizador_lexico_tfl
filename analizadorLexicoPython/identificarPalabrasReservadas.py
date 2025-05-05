from token_modelo import Token, Categoria

class IdentificarPalabrasReservadas:
    PALABRAS = {
        "abstract", "add", "alias", "as", "ascending", "async", "await", "base", "bool", "break", "by",
        "byte", "case", "catch", "char", "checked", "class", "const", "continue", "decimal", "default",
        "delegate", "descending", "do", "double", "dynamic", "else", "enum", "event", "explicit",
        "extern", "false", "finally", "fixed", "float", "for", "foreach", "from", "get", "global", "goto",
        "group", "if", "implicit", "in", "int", "interface", "internal", "into", "is", "join", "let",
        "lock", "long", "nameof", "namespace", "new", "null", "object", "on", "operator", "orderby",
        "out", "override", "params", "partial", "private", "protected", "public", "readonly", "ref",
        "remove", "return", "sbyte", "sealed", "select", "set", "short", "sizeof", "stackalloc", "static",
        "string", "struct", "switch", "this", "throw", "true", "try", "typeof", "uint", "ulong",
        "unchecked", "unsafe", "ushort", "using", "value", "var", "virtual", "void", "volatile", "when",
        "where", "while", "yield"
    }

    @staticmethod
    def extraer(codigo_fuente, indice):
        for palabra in sorted(IdentificarPalabrasReservadas.PALABRAS, key=len, reverse=True):
            fin = indice + len(palabra)
            if codigo_fuente[indice:fin] == palabra:
                if fin == len(codigo_fuente) or not codigo_fuente[fin].isalnum():
                    return Token(palabra, Categoria.PALABRA_RESERVADA, fin)
        return None
