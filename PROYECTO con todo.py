import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

#============================================================Codigo de diseño========================================================================
azul_principal = "#004d66"
azul_claro = "#e6f2f5"
blanco = "#ffffff"
gris = "#f7f7f7"
fuente_general = ("Helvetica", 11)
#================================================================Clases=========================================================================
class Persona:#"Clase padre 1"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class PersonalHospital:#"Clase padre 2"
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.ocupado = False

class Doctor(PersonalHospital):#"Clase hija 1" que hereda de la "Clase padre 2"
    pass

class Enfermero(PersonalHospital):#"Clase hija 2" que hereda de la "Clase padre 2"
    pass

class Paciente(Persona):#"Clase 3" que hereda de la "Clase 1"
    def __init__(self, nombre, edad, area, camilla, doctor, enfermero):
        super().__init__(nombre, edad)
        self.area = area
        self.camilla = camilla
        self.doctor = doctor
        self.enfermero = enfermero

#==============================================Codigo de la ventana secundaria de eleccion=================================================================0
def abrirseleccion():#funcion que permite abrir esta ventana
    ventanadeeleccion=tk.Toplevel(ventanaprincipal)
    ventanadeeleccion.title("SELECCION")
    ventanadeeleccion.geometry("420x300")
    ventanadeeleccion.configure(bg="#f0f4f7")

    #Muestra el encabezado
    encabezado = tk.Frame(ventanadeeleccion, bg=azul_principal, height=50)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Registro de Personas", fg="white", bg=azul_principal,font=("Helvetica", 16, "bold")).pack(pady=10)
    
    #Muestra el menu
    menu_seleccion = tk.Frame(ventanadeeleccion, width=150)
    menu_seleccion.pack()
    tk.Label(menu_seleccion, text="Menú", font=("Helvetica", 13, "bold")).pack(pady=20)


#==========================================Codigo de la ventana principal================================================================================0
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Hospital Ángeles - Plataforma")
ventanaprincipal.geometry("420x300")
ventanaprincipal.configure(bg="#e6f2f5")

titulo_font = font.Font(family="Helvetica", size=22, weight="bold")
eslogan_font = font.Font(family="Helvetica", size=12, slant="italic")
boton_font = font.Font(family="Helvetica", size=12)

tk.Label(ventanaprincipal, text="HOSPITAL ÁNGELES", font=titulo_font,fg="#004d66", bg="#e6f2f5").pack(pady=(30, 10))
tk.Label(ventanaprincipal, text="Donde la salud y el cuidado se encuentran",font=eslogan_font, fg="#006680", bg="#e6f2f5").pack(pady=(0, 30))

tk.Button(ventanaprincipal, text="Ingresar", font=boton_font,bg="#0080a1", fg="white", activebackground="#006680",activeforeground="white", width=15, height=2, command=abrirseleccion).pack()
tk.Button(ventanaprincipal, text="Salir", font=boton_font,bg="#0080a1", fg="white", activebackground="#006680",activeforeground="white", width=15, height=2, command=ventanaprincipal.destroy).pack()
ventanaprincipal.mainloop()
