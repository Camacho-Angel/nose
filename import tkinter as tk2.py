import tkinter as tk
from tkinter import ttk, messagebox

# Clases básicas
class Paciente:
    def __init__(self, nombre, edad, area, camilla, doctor, enfermero):
        self.nombre = nombre
        self.edad = edad
        self.area = area
        self.camilla = camilla
        self.doctor = doctor
        self.enfermero = enfermero

class Doctor:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

class Enfermero:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

# Datos iniciales
doctores = [
    Doctor("Dr. Pérez", "Urgencias"),
    Doctor("Dr. Gómez", "Hospitalización"),
]

enfermeros = [
    Enfermero("Enf. Martínez", "Urgencias"),
    Enfermero("Enf. López", "Hospitalización"),
]

camillas = {
    "Urgencias": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(3)],
    "Hospitalización": [{"ocupada": False, "doctor": None, "enfermero": None} for _ in range(5)],
}

pacientes = []

# Función para asignar camilla, doctor y enfermero
def asignar_camilla(area):
    for i, camilla in enumerate(camillas[area]):
        if not camilla["ocupada"]:
            camilla["ocupada"] = True
            # Asignar doctor y enfermero disponibles
            doc = next((d for d in doctores if d.area == area), None)
            enf = next((e for e in enfermeros if e.area == area), None)
            camilla["doctor"] = doc
            camilla["enfermero"] = enf
            return i+1, doc, enf
    return None, None, None

# Función para registrar paciente
def registrar_paciente():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    area = combo_area.get()

    if not nombre or not edad or not area:
        messagebox.showerror("Error", "Complete todos los campos")
        return
    try:
        edad = int(edad)
    except:
        messagebox.showerror("Error", "Edad debe ser un número")
        return

    camilla_num, doc, enf = asignar_camilla(area)
    if camilla_num is None:
        messagebox.showerror("Error", f"No hay camillas libres en {area}")
        return

    paciente = Paciente(nombre, edad, area, camilla_num, doc, enf)
    pacientes.append(paciente)
    messagebox.showinfo("Éxito", f"Paciente registrado en camilla {camilla_num} de {area}")

    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

# Funciones para mostrar tablas

def mostrar_pacientes():
    ventana = tk.Toplevel()
    ventana.title("Pacientes")

    cols = ("Nombre", "Edad", "Área", "Camilla", "Doctor", "Enfermero")
    tree = ttk.Treeview(ventana, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for p in pacientes:
        tree.insert("", tk.END, values=(
            p.nombre,
            p.edad,
            p.area,
            p.camilla,
            p.doctor.nombre if p.doctor else "N/A",
            p.enfermero.nombre if p.enfermero else "N/A"
        ))

    tree.pack(expand=True, fill=tk.BOTH)

def mostrar_doctores():
    ventana = tk.Toplevel()
    ventana.title("Doctores")

    cols = ("Nombre", "Área")
    tree = ttk.Treeview(ventana, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    for d in doctores:
        tree.insert("", tk.END, values=(d.nombre, d.area))

    tree.pack(expand=True, fill=tk.BOTH)

def mostrar_enfermeros():
    ventana = tk.Toplevel()
    ventana.title("Enfermeros")

    cols = ("Nombre", "Área")
    tree = ttk.Treeview(ventana, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    for e in enfermeros:
        tree.insert("", tk.END, values=(e.nombre, e.area))

    tree.pack(expand=True, fill=tk.BOTH)

# Ventana principal
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Hospital")

# Entradas para paciente
tk.Label(ventanaprincipal, text="Nombre Paciente:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventanaprincipal)
entry_nombre.grid(row=0, column=1)

tk.Label(ventanaprincipal, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(ventanaprincipal)
entry_edad.grid(row=1, column=1)

tk.Label(ventanaprincipal, text="Área:").grid(row=2, column=0)
combo_area = ttk.Combobox(ventanaprincipal, values=list(camillas.keys()))
combo_area.grid(row=2, column=1)

tk.Button(ventanaprincipal, text="Registrar Paciente", command=registrar_paciente).grid(row=3, column=0, columnspan=2)

# Botones para mostrar tablas
tk.Button(ventanaprincipal, text="Mostrar Pacientes", command=mostrar_pacientes).grid(row=4, column=0, sticky="ew")
tk.Button(ventanaprincipal, text="Mostrar Doctores", command=mostrar_doctores).grid(row=4, column=1, sticky="ew")
tk.Button(ventanaprincipal, text="Mostrar Enfermeros", command=mostrar_enfermeros).grid(row=5, column=0, columnspan=2, sticky="ew")

ventanaprincipal.mainloop()
