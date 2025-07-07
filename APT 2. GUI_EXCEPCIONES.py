
import tkinter as tk
from tkinter import messagebox

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

# Función de validación
def procesar_datos():
    try:
        nome = entrada_nome.get()
        apelidos = entrada_apelidos.get()
        documento_id = entrada_documento.get()
        data_nacemento = entrada_nacemento.get()
        peso_kg = float(entrada_peso.get())
        altura_cm = float(entrada_altura.get())
        data_ultima_consulta = entrada_ultima_consulta.get()

        paciente = Paciente(nome, apelidos, documento_id, data_nacemento, peso_kg, altura_cm, data_ultima_consulta)
        messagebox.showinfo("Paciente gardado", paciente.mostrar_info_paciente())

    except ValueError:
        messagebox.showerror("Erro", "Peso e altura deben ser números (usa punto para decimais se é necesario).")

# ------------------- DISEÑO CHULO -------------------
ventana = tk.Tk()
ventana.title("Ficha do Paciente")
ventana.configure(bg="#eaf4f4")
ventana.geometry("450x450")

titulo = tk.Label(ventana, text="Formulario de Rexistro de Pacientes", font=("Helvetica", 14, "bold"), bg="#eaf4f4", fg="#2c3e50")
titulo.pack(pady=10)

form_frame = tk.Frame(ventana, bg="#eaf4f4")
form_frame.pack(pady=5)

def crear_campo(label_text):
    fila = tk.Frame(form_frame, bg="#eaf4f4")
    fila.pack(pady=4)
    etiqueta = tk.Label(fila, text=label_text, width=25, anchor='w', bg="#eaf4f4")
    entrada = tk.Entry(fila, width=30)
    etiqueta.pack(side="left")
    entrada.pack(side="right")
    return entrada

entrada_nome = crear_campo("Nome:")
entrada_apelidos = crear_campo("Apelidos:")
entrada_documento = crear_campo("Documento ID:")
entrada_nacemento = crear_campo("Data nacemento (AAAA-MM-DD):")
entrada_peso = crear_campo("Peso (kg):")
entrada_altura = crear_campo("Altura (cm):")
entrada_ultima_consulta = crear_campo("Última consulta (AAAA-MM-DD):")

boton = tk.Button(ventana, text="📋 Gardar Paciente", bg="#2c3e50", fg="white", font=("Helvetica", 10, "bold"), width=25, height=2, command=procesar_datos)
boton.pack(pady=20)

ventana.mainloop()
