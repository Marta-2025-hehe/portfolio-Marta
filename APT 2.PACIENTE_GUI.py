#Este programa permite introducir datos de un paciente mediante una interfaz gráfica.
#Incluye:
#- Validación de fechas con strptime (formato YYYY-MM-DD)
#- Validación del DNI (formato y letra correcta)
#- Gestión de errores con messagebox
#- Interfaz mejorada con Tkinter



import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------------------
# Clase base Persona
# ---------------------------
class Persona:
    def __init__(self, nome, apelidos, documento_id, data_nacemento):
        self.nome = nome
        self.apelidos = apelidos
        self.documento_id = documento_id
        self.data_nacemento = data_nacemento

    def mostrar_info_persoal(self):
        return (f"Nome: {self.nome}\n"
                f"Apelidos: {self.apelidos}\n"
                f"Documento ID: {self.documento_id}\n"
                f"Data de nacemento: {self.data_nacemento}")

# ---------------------------
# Clase derivada Paciente
# ---------------------------
class Paciente(Persona):
    def __init__(self, nome, apelidos, documento_id, data_nacemento, peso_kg, altura_cm, data_ultima_consulta):
        super().__init__(nome, apelidos, documento_id, data_nacemento)
        self.peso_kg = peso_kg
        self.altura_cm = altura_cm
        self.data_ultima_consulta = data_ultima_consulta

    def mostrar_info_paciente(self):
        return (f"--- Información do Paciente ---\n"
                f"{self.mostrar_info_persoal()}\n"
                f"Peso: {self.peso_kg} kg\n"
                f"Altura: {self.altura_cm} cm\n"
                f"Última consulta: {self.data_ultima_consulta}")

# ---------------------------
# Función para validar DNI
# Verifica que el número tenga 8 cifras + 1 letra correcta
# ---------------------------
def validar_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) != 9:
        return False
    numero = dni[:-1]
    letra = dni[-1].upper()

    if not numero.isdigit():
        return False
    indice = int(numero) % 23
    return letras[indice] == letra

# ---------------------------
# Función principal que recoge los datos y valida
# ---------------------------
def procesar_datos():
    try:
        nome = entrada_nome.get()
        apelidos = entrada_apelidos.get()
        documento_id = entrada_documento.get().strip().upper()

        # Validación del DNI
        if not validar_dni(documento_id):
            raise ValueError("DNI incorrecto. Asegúrate de que el número y la letra son válidos.")
  
        # Validación de fechas con formato YYYY-MM-DD
        data_nacemento_raw = entrada_nacemento.get()
        data_nacemento = datetime.strptime(data_nacemento_raw, "%Y-%m-%d").date()

        data_ultima_raw = entrada_ultima_consulta.get()
        data_ultima_consulta = datetime.strptime(data_ultima_raw, "%Y-%m-%d").date()

        # Validación de números (peso y altura)
        peso_kg = float(entrada_peso.get())
        altura_cm = float(entrada_altura.get())

        # Creación de objeto Paciente
        paciente = Paciente(nome, apelidos, documento_id, data_nacemento, peso_kg, altura_cm, data_ultima_consulta)

        # Mostrar resultado final
        messagebox.showinfo("Paciente gardado", paciente.mostrar_info_paciente())

    except ValueError as e:
        # Si algo falla en la validación, se muestra el error
        messagebox.showerror("Erro de validación", str(e))

# ---------------------------
# Interfaz gráfica (GUI) con estilo visual
# ---------------------------
ventana = tk.Tk()
ventana.title("Ficha do Paciente")
ventana.configure(bg="#eaf4f4")
ventana.geometry("450x500")

titulo = tk.Label(ventana, text="Formulario de Rexistro de Pacientes", font=("Helvetica", 14, "bold"), bg="#eaf4f4", fg="#2c3e50")
titulo.pack(pady=10)

form_frame = tk.Frame(ventana, bg="#eaf4f4")
form_frame.pack(pady=5)

# Función para crear campos con etiqueta + entrada
def crear_campo(label_text, ayuda=""):
    fila = tk.Frame(form_frame, bg="#eaf4f4")
    fila.pack(pady=4)
    etiqueta = tk.Label(fila, text=label_text, width=25, anchor='w', bg="#eaf4f4")
    entrada = tk.Entry(fila, width=30)
    etiqueta.pack(side="left")
    entrada.pack(side="right")
    if ayuda:
        ayuda_lbl = tk.Label(form_frame, text=ayuda, font=("Helvetica", 7), fg="gray", bg="#eaf4f4", anchor="w")
        ayuda_lbl.pack()
    return entrada

# Campos del formulario
entrada_nome = crear_campo("Nome:")
entrada_apelidos = crear_campo("Apelidos:")
entrada_documento = crear_campo("Documento ID:", "Formato: 12345678Z")
entrada_nacemento = crear_campo("Data nacemento:", "Formato: AAAA-MM-DD")
entrada_peso = crear_campo("Peso (kg):")
entrada_altura = crear_campo("Altura (cm):")
entrada_ultima_consulta = crear_campo("Última consulta:", "Formato: AAAA-MM-DD")

# Botón principal
boton = tk.Button(ventana, text="📋 Gardar Paciente", bg="#2c3e50", fg="white", font=("Helvetica", 10, "bold"), width=25, height=2, command=procesar_datos)
boton.pack(pady=20)

ventana.mainloop()
