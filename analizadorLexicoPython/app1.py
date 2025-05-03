from tkinter import *
from ttkbootstrap import Window, Button, Treeview, Scrollbar, Label, Frame
from ttkbootstrap.constants import *
from analizador_lexico import AnalizadorLexico, Token, Categoria  # Importa las clases

def analizar_lexico():
    codigo = texto.get("1.0", END)  # Obtener el código fuente desde el Text widget
    analizador = AnalizadorLexico(codigo)  # Crear una instancia del analizador léxico
    analizador.analizar()  # Analizar el código fuente

    tokens = analizador.get_lista_tokens()  # Obtener los tokens encontrados

    # Limpiar la tabla y mostrar los tokens encontrados
    tabla_tokens.delete(*tabla_tokens.get_children())
    for token in tokens:
        # Mejorar el formato de la posición para incluir la línea y la columna
        line, col = calcular_posicion(codigo, token.indice_sgte)
        tabla_tokens.insert('', END, values=(token.palabra, token.categoria.name, f"Línea {line}, Col {col}"))

def calcular_posicion(codigo_fuente, indice):
    # Esta función calcula la línea y columna basadas en el índice
    line = 1
    col = 1
    for i in range(indice):
        if codigo_fuente[i] == '\n':
            line += 1
            col = 1
        else:
            col += 1
    return line, col

# Crear ventana
root = Window(themename="flatly")
root.title("Analizador Léxico")
root.geometry("600x500")

# Área de texto para el código fuente
Label(root, text="Código fuente:").pack(anchor=W, padx=10, pady=(10, 0))
texto = Text(root, height=10)
texto.pack(fill=X, padx=10)

# Botón para analizar
Button(root, text="Analizar Léxico", command=analizar_lexico, bootstyle=PRIMARY).pack(pady=10)

# Tabla de tokens
Label(root, text="Tokens encontrados:").pack(anchor=W, padx=10)

frame_tabla = Frame(root)
frame_tabla.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))

tabla_tokens = Treeview(frame_tabla, columns=("Lexema", "Categoría", "Posición"), show="headings")
tabla_tokens.heading("Lexema", text="Lexema")
tabla_tokens.heading("Categoría", text="Categoría")
tabla_tokens.heading("Posición", text="Posición")
tabla_tokens.column("Lexema", width=150)
tabla_tokens.column("Categoría", width=150)
tabla_tokens.column("Posición", width=200)
tabla_tokens.pack(side=LEFT, fill=BOTH, expand=True)

scroll = Scrollbar(frame_tabla, orient=VERTICAL, command=tabla_tokens.yview)
tabla_tokens.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

# Iniciar bucle de la aplicación
root.mainloop()
