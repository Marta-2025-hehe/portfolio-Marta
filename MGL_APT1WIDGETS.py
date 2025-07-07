# APT1 - Consulta a base de datos MySQL con interfaz gráfica (Tkinter)
# Alumna: Marta Glez. Lamas

import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk

# --- Datos de conexión a la base de datos ---
mi_servidor = "192.168.1.157"
mi_usuario = "SQL_boss"
mi_password = "MySQL_3982"
mi_bbdd = "world"

try:
    conexion = mysql.connector.connect(
        host=mi_servidor,
        user=mi_usuario,
        password=mi_password,
        database=mi_bbdd
    )

    if conexion.is_connected():
        print("¡Conexión exitosa!")

        def buscar_idioma():
            idioma_usuario = entrada_idioma.get()
            cursor = conexion.cursor()
            consulta = """
                SELECT 
                    country.Code, 
                    country.Name, 
                    countrylanguage.Language,
                    country.Population * (countrylanguage.Percentage / 100) AS NumHablantes
                FROM 
                    country
                JOIN 
                    countrylanguage 
                ON 
                    country.Code = countrylanguage.CountryCode
                WHERE 
                    countrylanguage.Language = %s
            """
            cursor.execute(consulta, (idioma_usuario,))
            resultados = cursor.fetchall()
            cursor.close()

            salida_texto.config(state="normal")
            salida_texto.delete("1.0", tk.END)

            if resultados:
                for fila in resultados:
                    salida_texto.insert(
                        tk.END,
                        f"País: {fila[1]} ({fila[0]})\nIdioma: {fila[2]}\nHablantes: {int(fila[3])}\n\n"
                    )
            else:
                salida_texto.insert(tk.END, "No se encontraron resultados para ese idioma.\n")

            salida_texto.config(state="disabled")

        # ---------------- VENTANA PRINCIPAL ----------------

        ventana = tk.Tk()
        ventana.title("MGL_APT1WIDGETS - Buscador de Idiomas por País")
        ventana.geometry("700x500")
        ventana.configure(bg="#f4f4f4")

        # Título principal
        titulo = tk.Label(
            ventana,
            text="Buscador de Idiomas por País",
            font=("Arial", 18, "bold"),
            bg="#f4f4f4",
            fg="#333"
        )
        titulo.pack(pady=15)

        # Etiqueta + campo de texto
        marco_input = tk.Frame(ventana, bg="#f4f4f4")
        marco_input.pack(pady=5)

        etiqueta = tk.Label(marco_input, text="Introduce un idioma:", font=("Arial", 12), bg="#f4f4f4")
        etiqueta.pack(side="left", padx=10)

        entrada_idioma = tk.Entry(marco_input, width=30, font=("Arial", 12))
        entrada_idioma.pack(side="left")

        # Botón de búsqueda
        boton_buscar = tk.Button(
            ventana,
            text="Buscar",
            command=buscar_idioma,
            bg="#add8e6",
            font=("Arial", 12)
        )
        boton_buscar.pack(pady=10)

        # Área de texto con scroll
        marco_texto = tk.Frame(ventana)
        marco_texto.pack(pady=10, fill="both", expand=True)

        salida_texto = tk.Text(marco_texto, wrap="word", font=("Consolas", 11), state="disabled")
        scroll = ttk.Scrollbar(marco_texto, command=salida_texto.yview)
        salida_texto.configure(yscrollcommand=scroll.set)

        salida_texto.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Iniciar GUI
        ventana.mainloop()

        # Cierre de conexión
        conexion.close()

except Error as e:
    print(f"Error al conectar con MySQL: {e}")
