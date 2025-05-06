import tkinter as tk
from tkinter import ttk
# Importación de módulos personalizados para el análisis léxico
from enteros_reales import tipo_numero
from identificadores import tipo_identificador
from palabrasReservadas import tipo_palabra_reservada
from operadoresAritmeticos import tipo_operador_aritmetico
from operadoresAsignacion import tipo_operador_asignacion
from operadoresComparacion import tipo_operador_comparacion
from operadoresLogicos import tipo_operador_logico
from IncremetoDecremento import tipo_operador_incremento_decremento
from parentesis import tipo_parentesis
from llaves import tipo_llave
from separador import tipo_separador
from terminalSentencia import tipo_terminal
from hexadecimal import tipo_hexadecimales
from comentariosLineaBloque import tipo_comentarios
from cadenas import tipo_cadenas

# Clase para la interfaz gráfica del Analizador Léxico


class AnalizadorLexicoGUI:
    def __init__(self):
        # Creación de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Analizador Lexico - Teoria lenguajes formales")
        # Dimensiones y posición de la ventana
        self.ancho_ventana = 450
        self.alto_ventana = 500
        self.posicion_x = 100
        self.posicion_y = 50

        dimensiones_ventana = "{}x{}+{}+{}".format(
            self.ancho_ventana, self.alto_ventana, self.posicion_x, self.posicion_y)
        self.ventana.geometry(dimensiones_ventana)

        # Crear el área de texto para ingresar el código a analizar
        self.entrada_texto = tk.Text(self.ventana, height=10, width=40)
        self.entrada_texto.pack(pady=10)

        # Crear el botón para activar el análisis léxico
        self.boton_agregar = tk.Button(
            self.ventana, text="Generar Analisis Lexico", command=self.realizar_analisis)
        self.boton_agregar.pack(pady=10)

        # Crear la tabla con tres columnas para mostrar los resultados del análisis
        self.columnas = ('Lexema', 'Categoria', 'Posicion')
        self.tabla = ttk.Treeview(
            self.ventana, columns=self.columnas, show='headings')

        # Configurar las columnas de la tabla
        for col in self.columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=130)

        self.tabla.pack(pady=20)

    # Método para realizar el análisis léxico
    def realizar_analisis(self):
        # Limpiar la tabla antes de mostrar nuevos resultados
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Obtener el texto ingresado en el área de texto
        texto = self.entrada_texto.get("1.0", tk.END).strip()

        # Realizar el análisis léxico invocando las funciones de los módulos importados
        resultados = []
        resultados += tipo_numero(texto)
        resultados += tipo_identificador(texto)
        resultados += tipo_palabra_reservada(texto)
        resultados += tipo_operador_aritmetico(texto)
        resultados += tipo_operador_logico(texto)
        resultados += tipo_operador_asignacion(texto)
        resultados += tipo_operador_comparacion(texto)
        resultados += tipo_operador_incremento_decremento(texto)
        resultados += tipo_parentesis(texto)
        resultados += tipo_llave(texto)
        resultados += tipo_separador(texto)
        resultados += tipo_terminal(texto)
        resultados += tipo_hexadecimales(texto)
        resultados += tipo_comentarios(texto)
        resultados += tipo_cadenas(texto)

        # Mostrar los resultados en la tabla de la interfaz gráfica
        for tipo, lexema, inicio, fin in resultados:
            self.tabla.insert('', 'end', values=(
                lexema, tipo, f"{inicio}-{fin}"))

    # Método para iniciar la aplicación y el bucle de eventos
    def iniciar(self):
        self.ventana.mainloop()
