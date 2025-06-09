import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

#=================================================Codigo de diseño=================================================================
azul_principal = "#004d66"
azul_claro = "#e6f2f5"
blanco = "#ffffff"
gris = "#f7f7f7"
fuente_general = ("Helvetica", 11)

#===========================================Librerias===========================================================================
#Donde se van a guardar todos los pacientes
pacientes_registrados = []
#Donde se van a guardar todos los doctores
doctores_registrados = []
#Donde se van a guardar todos los enfermeros
enfermeros_registrados = []

#=======================================================CLASES==================================================================
class Paciente:
    def __init__(self,nombre,apellidopa,apellidoma,genero,edad,curp,nss,estado,dias,fecha,meses,horarios):
          self.nombre=nombre
          self.apellidopa=apellidopa
          self.apellidoma=apellidoma
          self.genero=genero
          self.edad=edad
          self.curp=curp
          self.nss=nss
          self.estado=estado
          self.dias=dias
          self.fecha=fecha
          self.meses=meses
          self.horarios=horarios
    def __str__(self):
          return "Paciente registrado exitosamente" 

class Doctor:
    def __init__(self,nombred,apellidopad,apellidomad,generod,edadd,esped,aread,horariosd):
         self.nombred=nombred
         self.apellidopad=apellidopad
         self.apellidomad=apellidomad
         self.generod=generod
         self.edadd=edadd
         self.esped=esped
         self.aread=aread
         horariosd=horariosd
    def __str__(self):
         return "Doctor registrado exitosamente" 

class Enfermero:
    def __init__(self,nombreen,apellidopaen,apellidomaen,generoen,edaden,espeen,areaen,horariosen):
         self.nombreen=nombreen
         self.apellidopaen=apellidopaen
         self.apellidomaen=apellidomaen
         self.generoen=generoen
         self.edaden=edaden
         self.espeen=espeen
         self.areaen=areaen
         horariosen=horariosen
    def __str__(self):
         return "Enfermero registrado exitosamente"      
                   
#======================================CODIGO DE LA VENTANA SELECION====================================================
def abrirseleccion():
    ventanaseleccion=tk.Toplevel(ventanaprincipal)
    ventanaseleccion.title("Control de personas")
    ventanaseleccion.geometry("420x300")
    ventanaseleccion.configure(bg="#f0f4f7")

    #Muestra el encabezado
    encabezado = tk.Frame(ventanaseleccion, bg=azul_principal, height=50)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Registro de Personas", fg="white", bg=azul_principal,
             font=("Helvetica", 16, "bold")).pack(pady=10)
    
    #Muestra el menu
    menu_seleccion = tk.Frame(ventanaseleccion, width=150)
    menu_seleccion.pack()
    tk.Label(menu_seleccion, text="Menú", font=("Helvetica", 13, "bold")).pack(pady=20)

    #Muestra los botones del menu
    tk.Button(ventanaseleccion, text="Paciente", font=boton_font,
          bg="#0080a1", fg="white", activebackground="#006680",
          activeforeground="white", width=15, height=2, command=lambda: registropacientes(ventanaseleccion)).pack()
    
    tk.Button(ventanaseleccion, text="Doctor", font=boton_font,
          bg="#0080a1", fg="white", activebackground="#006680",
          activeforeground="white", width=15, height=2, command=lambda: registrodedoctores(ventanaseleccion)).pack()
    
    tk.Button(ventanaseleccion, text="Enfermero", font=boton_font,
          bg="#0080a1", fg="white", activebackground="#006680",
          activeforeground="white", width=15, height=2, command=registrodeenfermeros).pack()


#=============================================CODIGO DE LA VENTANA DE PACIENTES==============================================
#Codigo de la opcion pacientes
def registropacientes(ventanaseleccion):
    ventanaseleccion.withdraw() 
    ventanapaciente=tk.Toplevel()
    ventanapaciente.title("Plataforma de control de pacientes")
    # Encabezado
    encabezado = tk.Frame(ventanapaciente, bg=azul_principal, height=50)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Registro de Pacientes", fg="white", bg=azul_principal,
             font=("Helvetica", 16, "bold")).pack(pady=10)
    
    #Codigo de formulario
    tk.Label(ventanapaciente, text="Formulario de Registro", bg=blanco, font=("Helvetica", 14, "bold")).pack(pady=(0, 15))
    
    tk.Label(ventanapaciente, text="Nombres:", bg=blanco, font=fuente_general).pack()
    nombre = tk.Entry(ventanapaciente, font=fuente_general)
    nombre.pack()

    tk.Label(ventanapaciente, text="Apellido paterno:", bg=blanco, font=fuente_general).pack()
    apellidopa = tk.Entry(ventanapaciente, font=fuente_general)
    apellidopa.pack()

    tk.Label(ventanapaciente, text="Apellido materno:", bg=blanco, font=fuente_general).pack()
    apellidoma = tk.Entry(ventanapaciente, font=fuente_general)
    apellidoma.pack()

    tk.Label(ventanapaciente, text="Genero:", bg=blanco, font=fuente_general).pack()
    genero = tk.Entry(ventanapaciente, font=fuente_general)
    genero.pack()

    tk.Label(ventanapaciente, text="Edad:", bg=blanco, font=fuente_general).pack()
    edad = tk.Entry(ventanapaciente, font=fuente_general)
    edad.pack()

    tk.Label(ventanapaciente, text="CURP:", bg=blanco, font=fuente_general).pack()
    curp = tk.Entry(ventanapaciente, font=fuente_general)
    curp.pack()

    tk.Label(ventanapaciente, text="Numero de Seguridad Social:", bg=blanco, font=fuente_general).pack()
    nss = tk.Entry(ventanapaciente, font=fuente_general)
    nss.pack()

    tk.Label(ventanapaciente, text="Estado del paciente:", bg=blanco, font=fuente_general).pack()
    estado = tk.Entry(ventanapaciente, font=fuente_general)
    estado.pack()

    tk.Label(ventanapaciente, text="Día:", bg=blanco, font=fuente_general).pack()
    dias = ttk.Combobox(ventanapaciente, values=["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"])
    dias.pack()
    dias.current(0)

    tk.Label(ventanapaciente, text="Fecha:", bg=blanco, font=fuente_general).pack()
    fecha = ttk.Combobox(ventanapaciente, values=[str(i) for i in range(1, 32)])
    fecha.pack()
    fecha.current(0)

    tk.Label(ventanapaciente, text="Mes:", bg=blanco, font=fuente_general).pack()
    meses = ttk.Combobox(ventanapaciente, values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                                                    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
    meses.pack()
    meses.current(0)

    tk.Label(ventanapaciente, text="Horario:", bg=blanco, font=fuente_general).pack()
    horarios = ttk.Combobox(ventanapaciente, values=["Matutino", "Vespertino", "Nocturno"])
    horarios.pack()
    horarios.current(0)

    def guardar():
        paciente = Paciente(
         nombre.get(),
         apellidopa.get(),
         apellidoma.get(),
         genero.get(),
         edad.get(),
         curp.get(),
         nss.get(),
         estado.get(),
         dias.get(),
         fecha.get(),
         meses.get(),
         horarios.get()
    )
        pacientes_registrados.append(paciente)  # ← Aquí se guarda el paciente
    # Mostrar mensaje de confirmación
        messagebox.showinfo("Registro exitoso", str(paciente))  
     
    def repetir():
        nombre.delete(0, tk.END)
        apellidopa.delete(0, tk.END)
        apellidoma.delete(0,tk.END)
        genero.delete(0,tk.END)
        edad.delete(0,tk.END)
        curp.delete(0,tk.END)
        nss.delete(0,tk.END)
        estado.delete(0,tk.END)
    def regresar():
        ventanapaciente.destroy()
        ventanaseleccion.deiconify()
            
    tk.Button(ventanapaciente, text="Guardar Registro", font=fuente_general,
                  bg="#0080a1", fg="white", activebackground="#006680", activeforeground="white",
                  command=guardar).pack(pady=10)

    tk.Button(ventanapaciente,text="Repetir", font=fuente_general,
                  bg="#0080a1", fg="white", activebackground="#006680", activeforeground="white",
                  command=repetir).pack()
    
    menupacientes=tk.Menu(ventanapaciente)
    opciones= tk.Menu(menupacientes, tearoff=0)
    opciones.add_command(label="Regresar", command=regresar)
    menupacientes.add_cascade(label="Opciones", menu=opciones)
    ventanapaciente.config(menu=menupacientes)

#===============================================================CODIGO DE LA OPCION DOCTORES====================================================================================
def registrodedoctores(ventanaseleccion):  
    ventanaseleccion.withdraw() 
    ventanadoctores=tk.Toplevel() 
    ventanadoctores.title("Plataforma de control de doctores")
# Encabezado
    encabezado = tk.Frame(ventanadoctores, bg=azul_principal, height=50)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Registro de Doctores", fg="white", bg=azul_principal,
             font=("Helvetica", 16, "bold")).pack(pady=10)
    
    #Codigo de formulario
    tk.Label(ventanadoctores, text="Formulario de Registro", bg=blanco, font=("Helvetica", 14, "bold")).pack(pady=(0, 15))
    
    tk.Label(ventanadoctores, text="Nombres:", bg=blanco, font=fuente_general).pack()
    nombred = tk.Entry(ventanadoctores, font=fuente_general)
    nombred.pack()

    tk.Label(ventanadoctores, text="Apellido paterno:", bg=blanco, font=fuente_general).pack()
    apellidopad = tk.Entry(ventanadoctores, font=fuente_general)
    apellidopad.pack()

    tk.Label(ventanadoctores, text="Apellido materno:", bg=blanco, font=fuente_general).pack()
    apellidomad = tk.Entry(ventanadoctores, font=fuente_general)
    apellidomad.pack()

    tk.Label(ventanadoctores, text="Genero:", bg=blanco, font=fuente_general).pack()
    generod = tk.Entry(ventanadoctores, font=fuente_general)
    generod.pack()

    tk.Label(ventanadoctores, text="Edad:", bg=blanco, font=fuente_general).pack()
    edadd = tk.Entry(ventanadoctores, font=fuente_general)
    edadd.pack()

    tk.Label(ventanadoctores, text="Especialidad:", bg=blanco, font=fuente_general).pack()
    esped = ttk.Combobox(ventanadoctores, values=["Medicina Interna", "Pediatria", "Ginecologia", "Cirugia General", "Anesteciologia", "Cardiologia", "Psiquiatria", "Ninguna"])
    esped.pack()
    esped.current(0)

    tk.Label(ventanadoctores, text="Area:", bg=blanco, font=fuente_general).pack()
    aread = ttk.Combobox(ventanadoctores, values=["Urgencias","Hospitalizacion","Unidad de Cuidados Intensivos","Visitas","Consulta"])
    aread.pack()
    aread.current(0)

    tk.Label(ventanadoctores, text="Horario:", bg=blanco, font=fuente_general).pack()
    horariosd = ttk.Combobox(ventanadoctores, values=["Matutino", "Vespertino", "Nocturno"])
    horariosd.pack()
    horariosd.current(0)

    def guardar2():
        doctor = Doctor(
         nombred.get(),
         apellidopad.get(),
         apellidomad.get(),
         generod.get(),
         edadd.get(),
         esped.get(),
         aread.get(),
         horariosd.get()
    )
        doctores_registrados.append(doctor)  # ← Aquí se guarda el doctor
    # Mostrar mensaje de confirmación
        messagebox.showinfo("Registro exitoso", str(doctor))
    #Funcion de boton de repetir
    def repetir2():
         nombred.delete(0, tk.END)
         apellidopad.delete(0, tk.END)
         apellidomad.delete(0,tk.END)
         generod.delete(0,tk.END)
         edadd.delete(0,tk.END)
    
    def regresar():
        ventanadoctores.destroy()
        ventanaseleccion.deiconify()    

    tk.Button(ventanadoctores, text="Guardar Registro", font=fuente_general,
                  bg="#0080a1", fg="white", activebackground="#006680", activeforeground="white",
                  command=guardar2).pack(pady=10)

    tk.Button(ventanadoctores,text="Repetir", font=fuente_general,
                  bg="#0080a1", fg="white", activebackground="#006680", activeforeground="white",
                  command=repetir2).pack()
    menudoctores=tk.Menu(ventanadoctores)
    opciones= tk.Menu(menudoctores, tearoff=0)
    opciones.add_command(label="Regresar", command=regresar)
    menudoctores.add_cascade(label="Opciones", menu=opciones)
    ventanadoctores.config(menu=menudoctores)

  

#Codigo de la opcion enfermeros
def registrodeenfermeros():  
    ventanaenfermeros=tk.Toplevel() 
    ventanaenfermeros.title("Plataforma de control de enfermeros")
    # Encabezado
    encabezado = tk.Frame(ventanaenfermeros, bg=azul_principal, height=50)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Registro de Doctores", fg="white", bg=azul_principal,
             font=("Helvetica", 16, "bold")).pack(pady=10)
    
    #Codigo de formulario
    tk.Label(ventanaenfermeros, text="Formulario de Registro", bg=blanco, font=("Helvetica", 14, "bold")).pack(pady=(0, 15))
    
    tk.Label(ventanaenfermeros, text="Nombres:", bg=blanco, font=fuente_general).pack()
    nombreen = tk.Entry(ventanaenfermeros, font=fuente_general)
    nombreen.pack()

    tk.Label(ventanaenfermeros, text="Apellido paterno:", bg=blanco, font=fuente_general).pack()
    apellidopaen = tk.Entry(ventanaenfermeros, font=fuente_general)
    apellidopaen.pack()

    tk.Label(ventanaenfermeros, text="Apellido materno:", bg=blanco, font=fuente_general).pack()
    apellidomaen = tk.Entry(ventanaenfermeros, font=fuente_general)
    apellidomaen.pack()

    tk.Label(ventanaenfermeros, text="Genero:", bg=blanco, font=fuente_general).pack()
    generoen = tk.Entry(ventanaenfermeros, font=fuente_general)
    generoen.pack()

    tk.Label(ventanaenfermeros, text="Edad:", bg=blanco, font=fuente_general).pack()
    edaden = tk.Entry(ventanaenfermeros, font=fuente_general)
    edaden.pack()

    tk.Label(ventanaenfermeros, text="Especialidad:", bg=blanco, font=fuente_general).pack()
    espeen = ttk.Combobox(ventanaenfermeros, values=["Medico-Quirurgica", "Cuidados Intensivos", "Obstetrico-Ginecologia", "Pediatrica", "Instrumentista y Circulante","Ninguna"])
    espeen.pack()
    espeen.current(0)

    tk.Label(ventanaenfermeros, text="Area:", bg=blanco, font=fuente_general).pack()
    areaen = ttk.Combobox(ventanaenfermeros, values=["Urgencias","Hospitalizacion","Unidad de Cuidados Intensivos","Visitas","Consulta"])
    areaen.pack()
    areaen.current(0)

    tk.Label(ventanaenfermeros, text="Horario:", bg=blanco, font=fuente_general).pack()
    horariosen = ttk.Combobox(ventanaenfermeros, values=["Matutino", "Vespertino", "Nocturno"])
    horariosen.pack()
    horariosen.current(0)

    def guardar3():
        enfermero = Enfermero(
         nombreen.get(),
         apellidopaen.get(),
         apellidomaen.get(),
         generoen.get(),
         edaden.get(),
         espeen.get(),
         areaen.get(),
         horariosen.get()
    )
        enfermeros_registrados.append(enfermero)  # ← Aquí se guarda el enfermero
    # Mostrar mensaje de confirmación
        messagebox.showinfo("Registro exitoso", str(enfermero))
    def repetir3():
         nombreen.delete(0, tk.END)
         apellidopaen.delete(0, tk.END)
         apellidomaen.delete(0,tk.END)
         generoen.delete(0,tk.END)
         edaden.delete(0,tk.END)

    tk.Button(ventanaenfermeros, text="Guardar Registro", font=fuente_general,
                  bg="#0080a1", fg="white", activebackground="#006680", activeforeground="white",
                  command=guardar3).pack(pady=10)

    tk.Button(ventanaenfermeros,text="Repetir", font=fuente_general,
                  bg="#0080a1", fg="white", activebackground="#006680", activeforeground="white",
                  command=repetir3).pack()

#==========================================Codigo de la ventana principal===================================================
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Hospital Ángeles - Plataforma")
ventanaprincipal.geometry("420x300")
ventanaprincipal.configure(bg="#e6f2f5")

titulo_font = font.Font(family="Helvetica", size=22, weight="bold")
eslogan_font = font.Font(family="Helvetica", size=12, slant="italic")
boton_font = font.Font(family="Helvetica", size=12)

tk.Label(ventanaprincipal, text="HOSPITAL ÁNGELES", font=titulo_font,
         fg="#004d66", bg="#e6f2f5").pack(pady=(30, 10))
tk.Label(ventanaprincipal, text="Donde la salud y el cuidado se encuentran",
         font=eslogan_font, fg="#006680", bg="#e6f2f5").pack(pady=(0, 30))

tk.Button(ventanaprincipal, text="Ingresar", font=boton_font,
          bg="#0080a1", fg="white", activebackground="#006680",
          activeforeground="white", width=15, height=2, command=abrirseleccion).pack()
tk.Button(ventanaprincipal, text="Salir", font=boton_font,
          bg="#0080a1", fg="white", activebackground="#006680",
          activeforeground="white", width=15, height=2, command=ventanaprincipal.destroy).pack()

ventanaprincipal.mainloop()