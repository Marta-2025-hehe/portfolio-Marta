# APT1 - Conexión a BBDD MySQL y consulta SQL con filtro por idioma
# Alumna: Marta Glez. Lamas

import mysql.connector
from mysql.connector import Error

# --- Datos de conexión a la base de datos ---
# Si lo quisieras hacer interactivo, podrías usar input(), pero aquí están fijos:
"""
mi_servidor = input("Servidor: ")
mi_usuario = input("Usuario: ")
mi_password = input("Password: ")
mi_bbdd = input("Base de datos: ")
"""

# Datos de conexión a la base de datos MySQL (phpMyAdmin en local o red)
mi_servidor = "192.168.1.157"
mi_usuario = "SQL_boss"
mi_password = "MySQL_3982"
mi_bbdd = "world"

try:
    # Establece conexión con la base de datos
    conexion = mysql.connector.connect(
        host=mi_servidor,
        user=mi_usuario,
        password=mi_password,
        database=mi_bbdd
    )

    # Si la conexión es exitosa
    if conexion.is_connected():
        print("¡Conexión exitosa!")

        # Solicita al usuario el idioma por consola
        idioma_usuario = input("Introduce un idioma (por ejemplo: Spanish): ")

        # Crear cursor para ejecutar la consulta
        cursor = conexion.cursor()

        # Consulta SQL para obtener datos del país e idioma y calcular hablantes
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

        # Ejecutar la consulta con el idioma proporcionado
        cursor.execute(consulta, (idioma_usuario,))
        resultados = cursor.fetchall()

        # Mostrar los resultados en consola
        print("\n📋 RESULTADOS:")
        for fila in resultados:
            print(f"Code: {fila[0]}, Name: {fila[1]}, Language: {fila[2]}, Hablantes: {int(fila[3])}")

        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()

# Si ocurre algún error durante la conexión
except Error as e:
    print(f"Error al conectar con MySQL: {e}")
