# Analizador Léxico TFL

Un Analizador Léxico basado en Autómatas Finitos Deterministas, desarrollado en Python como parte de la asignatura de Teoría de Lenguajes Formales (TFL) de la carrera de Ingeniería de Sistemas y Computación. Su propósito es procesar código fuente de un lenguaje de programación sencillo, reconocer y clasificar los distintos tokens (números, identificadores, palabras reservadas, operadores, símbolos, cadenas y comentarios) mediante autómatas bien definidos y mostrar gráficamente el flujo de estados.

---

## 1. Visión general

El proyecto implementa un conjunto completo de autómatas finitos deterministas (AFD), uno por cada categoría de token:

- **Números naturales**: reconoce secuencias no vacías de dígitos (`D+`).
- **Números reales**: reconoce parte entera y fraccionaria separadas por punto (`D+(\.D+)`).
- **Identificadores**: letras y guion bajo iniciales, seguidos de letras, dígitos o guion bajo (`[a-zA-Z_][a-zA-Z0-9_]*`).
- **Palabras reservadas**: autómatas lineales para cada palabra (e.g. `try`, `class`, `for`).
- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `%`.
- **Operadores de comparación**: `==`, `!=`, `>=`, `<=`, `>`, `<`.
- **Operadores lógicos**: `&&`, `||`, `!`.
- **Operadores de asignación compuestos**: `+=`, `-=`, `*=`, `/=`, `%=`.
- **Operadores de incremento/decremento**: `++`, `--`.
- **Delimitadores y símbolos**: `{}`, `()`, `;`, `,`.
- **Cadenas de caracteres**: literales entre comillas dobles (`"([^"\n])*"`).
- **Comentarios de línea**: desde `//` hasta fin de línea.
- **Comentarios de bloque**: desde `/*` hasta `*/`, incluyendo anidamientos simples.

Cada autómata consta de un diagrama de estados y una breve descripción funcional, acompañados de ejemplos de cadenas aceptadas.

---

## 2. Características principales

- **Diseño modular**  
  Cada categoría de token se implementa como un módulo independiente, facilitando la extensión y mantenimiento.

- **Interfaz gráfica**  
  Basada en `ttkbootstrap` para proporcionar controles modernos y ligeros.  
  Permite cargar un archivo de código, seleccionar el autómata correspondiente y observar en tiempo real la transición de estados.

- **Expresiones regulares y descripciones**  
  Para cada autómata se documenta la expresión regular asociada y su lógica interna, asegurando trazabilidad entre especificación y código.

- **Pruebas unitarias**  
  Conjunto de tests automáticos que verifican el reconocimiento correcto de cadenas válidas e inválidas para cada token.

- **Fácil integración**  
  Diseñado para incorporarse en proyectos más amplios de compiladores o intérpretes como módulo de análisis léxico.

---

## 3. Requisitos

- Python 3.8 o superior  
- Windows PowerShell (para activar el entorno virtual en sistemas Windows)  
- Conexión a Internet para instalar paquetes mediante `pip`

---

## 4. Instalación y configuración

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/CapitanWid/analizador_lexico_tfl.git
   cd analizador_lexico_tfl

2. **Abrir en Visual Studio Code**

   En VS Code, seleccione **File → Open Folder…** y apunte a la carpeta del proyecto.

3. **Abrir terminal integrada**

   Haga clic en los tres puntos (⋯) de la barra inferior y seleccione **New Terminal**.

4. **Crear y activar el entorno virtual**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1

5. **Instalar dependencias**
   ```bash
   pip install ttkbootstrap

---

## 5. Ejecución de la aplicación

Con el entorno virtual activado:
   ```bash
   python app1.py

1. **Se desplegará una ventana gráfica.**

2. **Cargar un archivo de código fuente (.txt, .py, etc.).**

3. **Seleccionar el autómata que se desea probar.**

4. **Observar la animación de estados conforme se reconoce cada token.**

---

## 6. Estructura del repositorio
   ```bash
   analizador_lexico_tfl/

   │
   ├── app1.py                  # Punto de entrada con interfaz gráfica
   ├── automatas/               # Implementación de cada autómata
   │   ├── naturales.py
   │   ├── reales.py
   │   ├── identificadores.py
   │   ├── palabras_reservadas.py
   │   ├── operadores_aritmeticos.py
   │   └── ...
   ├── utils/                   # Funciones auxiliares (lectura de archivo, logging, GUI helpers)
   ├── tests/                   # Pruebas unitarias (pytest)
   │   ├── test_naturales.py
   │   ├── test_identificadores.py
   │   └── ...
   ├── venv/                    # Entorno virtual (excluido del control de versiones)
   ├── README.md                # Documentación del proyecto
   └── LICENSE                  # Licencia MIT

---

## 7. Pruebas

Se recomienda ejecutar todas las pruebas antes y después de realizar cambios significativos:
   ```bash
   pytest tests/

---

## 8. Contribuciones

Las contribuciones son bienvenidas. Para colaborar:

1. **Fork del repositorio.**

2. **Crear una rama con la nueva funcionalidad o corrección:**
   ```bash
   git checkout -b feature/nueva-funcionalidad

3. **Realizar commits claros y descriptivos.**

4. **Abrir un Pull Request describiendo el cambio y su motivación.**

---

## 9. Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.

Desarrollado como proyecto final de la asignatura de Teoría de Lenguajes Formales, Universidad del Quindío.

---