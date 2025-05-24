# analizador_lexico.py
from identificarEnteros import IdentificarEnteros
from identificarReales import IdentificarReales
from identificarIdentificadores import IdentificarIdentificadores
from identificarPalabrasReservadas import IdentificarPalabrasReservadas
from identificarOperadoresAritmeticos import IdentificarOperadoresAritmeticos
from identificarOperadoresComparacion import IdentificarOperadoresComparacion
from identificarOperadoresLogicos import IdentificarOperadoresLogicos
from identificarOperadoresAsignacion import IdentificarOperadoresAsignacion
from identificarIncrementoDecremento import IdentificarIncrementoDecremento
from identificarParentesis import IdentificarParentesis
from identificarLlaves import IdentificarLlaves
from identificarCorchetes import IdentificarCorchetes
from identificarTerminal import IdentificarTerminal
from identificarSeparador import IdentificarSeparador
from identificarCadenaCaracteres import IdentificarCadenaCaracteres
from identificarComentarios import IdentificarComentarios
from token_modelo import Categoria, Token

class AnalizadorLexico:
    def __init__(self, codigo_fuente):
        self.codigo_fuente = codigo_fuente
        self.lista_tokens = []

        # Lista de analizadores en orden de prioridad
        self.analizadores = [
            IdentificarReales,
            IdentificarEnteros,
            IdentificarPalabrasReservadas,
            IdentificarIdentificadores,
            IdentificarOperadoresComparacion,
            IdentificarOperadoresAsignacion,
            IdentificarIncrementoDecremento,
            IdentificarOperadoresLogicos,
            IdentificarComentarios,
            IdentificarOperadoresAritmeticos,
            IdentificarCadenaCaracteres,
            IdentificarParentesis,
            IdentificarLlaves,
            IdentificarCorchetes,
            IdentificarTerminal,
            IdentificarSeparador,
        ]

    def analizar(self):
        i = 0
        while i < len(self.codigo_fuente):
                    # Ignorar espacios en blanco, tabs y saltos de línea
            if self.codigo_fuente[i] in {' ', '\t', '\n', '\r'}:
                i += 1
                continue #para avanzar al siguiente caracter a analizar

            token = self.extraer_sgte_token(i)
            if token:
                self.lista_tokens.append(token)
                i = token.indice_sgte
            else:
                i += 1

    def extraer_sgte_token(self, indice):
        for analizador in self.analizadores:
            token = analizador.extraer(self.codigo_fuente, indice)
            if token:
                return token

        return self.extraer_no_reconocido(indice)

    def extraer_no_reconocido(self, indice):
        lexema = self.codigo_fuente[indice]
        return Token(lexema, Categoria.NO_RECONOCIDO,indice, indice + 1)

    def get_lista_tokens(self):
        return self.lista_tokens