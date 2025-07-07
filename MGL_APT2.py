# APT2 - Consulta a un Web Service REST para convertir divisas a euros
# Alumna: Marta Glez. Lamas

import requests  # Librería para hacer peticiones HTTP (GET, POST, etc.)

# URL del servicio de cambio de divisas (devuelve JSON con tasas respecto al dólar)
url = "https://cdn.dinero.today/api/latest.json"

try:
    # Realizamos una petición GET al servicio web
    respuesta = requests.get(url)

    # Convertimos la respuesta en formato JSON (diccionario en Python)
    datos = respuesta.json()

    # Validamos que la petición fue exitosa y que contiene el bloque "rates"
    if respuesta.status_code == 200 and "rates" in datos:
        rates = datos["rates"]  # Extraemos el diccionario de tipos de cambio

        # --- Entrada de datos por parte del usuario ---
        # Código de la moneda original (ej: JPY, USD, GBP, etc.)
        divisa_origen = input("Introduce el código de la divisa de origen (por ejemplo: JPY): ").upper()
        # Importe que se quiere convertir
        importe = float(input("Introduce el importe en esa divisa: "))

        # Validamos que el código de divisa introducido existe en los datos del servicio
        if divisa_origen in rates and "EUR" in rates:
            cambio_origen = rates[divisa_origen]  # Cuántas unidades de esa divisa equivalen a 1 USD
            cambio_eur = rates["EUR"]             # Cuántas unidades de EUR equivalen a 1 USD

            # --- Conversión de importes ---
            # 1. Convertimos el importe original a USD
            importe_en_usd = importe / cambio_origen
            # 2. Convertimos ese importe en USD a euros
            importe_en_eur = importe_en_usd * cambio_eur

            # --- Salida por consola ---
            print(f"\nTipo de cambio respecto a USD para {divisa_origen}: {cambio_origen}")
            print(f"Importe equivalente en euros: {importe_en_eur:.2f} EUR")

        else:
            # Si la divisa no está en la lista de tasas
            print("❌ La divisa introducida no está disponible en el servicio.")
    else:
        # Si hubo un problema al procesar el JSON o la respuesta
        print("❌ Error al obtener los datos del servicio.")

except requests.exceptions.RequestException as e:
    # Captura de errores de conexión, timeout, etc.
    print(f"❌ Error al conectar con el servicio: {e}")
