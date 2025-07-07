# APT2 - Interfaz gráfica para convertir divisas a euros usando un Web Service
# Alumna: Marta Glez. Lamas

import requests            # Librería para hacer peticiones HTTP a servicios web (REST API)
import tkinter as tk       # Librería estándar de Python para construir interfaces gráficas (GUI)

# ---------------- FUNCIONALIDAD PRINCIPAL ------------------

def obtener_cambio():
    # Obtener el código de divisa introducido por el usuario y convertirlo a mayúsculas
    divisa_origen = entrada_divisa.get().upper()

    # Validación del importe (debe ser numérico)
       # Validación del importe (debe ser numérico)
    try:
        importe = float(entrada_importe.get().replace(",", "."))
    except ValueError:
        salida_texto.config(text="❌ Importe inválido. Introduce un número.")
        return
    # URL del servicio REST de tasas de cambio (retorna JSON con cambios respecto a USD)
    url = "https://cdn.dinero.today/api/latest.json"

    try:
        # Realizamos la solicitud HTTP GET al servicio web
        respuesta = requests.get(url)
        datos = respuesta.json()

        # Validamos que la respuesta sea correcta y tenga datos de tasas de cambio
        if respuesta.status_code == 200 and "rates" in datos:
            rates = datos["rates"]  # Diccionario de tasas de cambio

            # Verificamos que exista la divisa indicada y el euro
            if divisa_origen in rates and "EUR" in rates:
                cambio_origen = rates[divisa_origen]  # Valor de la divisa respecto a USD
                cambio_eur = rates["EUR"]             # Valor del euro respecto a USD

                # Paso 1: Convertir el importe de origen a dólares (USD)
                importe_usd = importe / cambio_origen

                # Paso 2: Convertir el importe en USD a euros
                importe_eur = importe_usd * cambio_eur

                # Resultado formateado que se muestra en pantalla
                resultado = (
                    f"Tipo de cambio {divisa_origen} → USD: {cambio_origen:.4f}\n"
                    f"Importe equivalente en EUR: {importe_eur:.2f} €"
                )
                salida_texto.config(text=resultado)
            else:
                # Si el código de divisa no está en la respuesta
                salida_texto.config(text="❌ Divisa no disponible en el servicio.")
        else:
            # Error en la respuesta del servicio
            salida_texto.config(text="❌ Error al obtener los datos del servicio.")
    except requests.exceptions.RequestException as e:
        # Error en la conexión a Internet o al servicio
        salida_texto.config(text=f"❌ Error de conexión: {e}")

# ---------------- INTERFAZ TKINTER ------------------

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("MGL_APT2WIDGETS - Conversor a EUR")  # Título de la ventana
ventana.geometry("400x250")  # Tamaño de la ventana

# Etiqueta y campo de entrada para el código de divisa (ej: JPY, USD, GBP)
tk.Label(ventana, text="Introduce código de divisa:", font=("Arial", 11)).pack(pady=5)
entrada_divisa = tk.Entry(ventana)
entrada_divisa.pack(pady=5)

# Etiqueta y campo de entrada para el importe numérico
tk.Label(ventana, text="Introduce importe:", font=("Arial", 11)).pack(pady=5)
entrada_importe = tk.Entry(ventana)
entrada_importe.pack(pady=5)

# Botón para ejecutar la conversión
tk.Button(
    ventana,
    text="Convertir a EUR",
    command=obtener_cambio,
    bg="lightgreen"
).pack(pady=10)

# Área de salida para mostrar el resultado final
salida_texto = tk.Label(ventana, text="", font=("Arial", 11), fg="blue", justify="center")
salida_texto.pack(pady=10)

# Inicia el bucle principal de eventos de la interfaz
ventana.mainloop()
